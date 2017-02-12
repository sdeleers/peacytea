local_production.py contains the database secrets and the Django secret key, and therefore should not be committed.
It should contain the following variables that are used in production.py:

DB_NAME
DB_USER
DB_PWD
SECRET_KEY
ALLOWED_HOSTS