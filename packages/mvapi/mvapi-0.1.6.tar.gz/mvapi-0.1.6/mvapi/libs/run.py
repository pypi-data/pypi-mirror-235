from bdb import BdbQuit

from blinker import signal
from click.exceptions import Abort, ClickException, Exit

from mvapi.cli.project import cli
from mvapi.libs.database import db
from mvapi.libs.error import save_error
from mvapi.libs.logger import init_logger
from mvapi.models import import_models
from mvapi.web.libs.appfactory import create_app
from mvapi.web.serializers import import_serializers
from mvapi.web.views import import_views

before_app_create = signal('mvapi.before_app_create')


def run_app(cli_=cli):
    import_models()
    import_views()
    import_serializers()
    init_logger()

    before_app_create.send(None)

    if not cli_:
        return create_app()
    else:
        try:
            cli_.main(standalone_mode=False)
            db.session.commit()
        except ClickException as exc:
            exc.show()
        except (Abort, Exit, BdbQuit):
            db.session.rollback()
        except Exception as exc:
            db.session.rollback()
            save_error()
            raise exc
        finally:
            db.session.remove()
