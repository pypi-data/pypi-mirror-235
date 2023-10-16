import re

from setuptools import find_packages, setup

with open('./mvapi/version.py') as file:
    version = re.search(r'version = \'(.*?)\'', file.read()).group(1)

setup(
    name='mvapi',
    version=version,
    description='Skeleton for a JSON API project',
    license='GNU General Public License v3 (GPLv3)',
    url='https://github.com/mvetoshkin/mvapi',
    author='Mikhail Vetoshkin',
    author_email='mikhail@vetoshkin.dev',
    packages=find_packages(),
    package_data={
        '': ['templates/*']
    },
    entry_points={
        'console_scripts': [
            'mvapi = mvapi:main'
        ]
    },
    install_requires=[
        'alembic == 1.7.5',
        'bcrypt == 3.2.0',
        'blinker == 1.5',
        'click == 8.0.3',
        'flask == 2.0.2',
        'flask-cors == 3.0.10',
        'inflect == 5.4.0',
        'jinja2 == 3.0.3',
        'psycopg2 == 2.9.3',
        'pyjwt == 2.3.0',
        'python-dateutil==2.8.2',
        'python-dotenv == 0.19.1',
        'shortuuid == 1.0.8',
        'sqlalchemy == 1.4.28',
        'validate-email == 1.3',
        'werkzeug == 2.1.0',
    ],
    python_requires='>=3.9',
)
