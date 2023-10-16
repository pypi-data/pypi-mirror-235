import click

from mvapi.libs.exceptions import NotFoundError
from mvapi.libs.logger import logger
from mvapi.web.models.user import User


@click.command('update-user')
@click.option('--email', required=True, help='user email')
@click.option('--is-admin/--not-admin', default=None, help='admin flag')
@click.password_option(help='user password')
def update_user(email, password, is_admin):
    """Update a user"""

    try:
        user = User.query.get_by(email=email)
    except NotFoundError:
        logger.info(f'User with email {email} not found')
        return

    if password:
        user.password = password

    if is_admin is not None:
        user.is_admin = is_admin

    logger.info(f'User {user} updated')
