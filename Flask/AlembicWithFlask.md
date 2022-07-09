# Setup Database

1. Open psql: `sudo -u postgres psql`
1. Create user: `CREATE USER flask_migrate_test WITH PASSWORD 'flask_migrate_test';`
1. Create DB: `CREATE DATABASE flask_migrate_test WITH OWNER flask_migrate_test;`

# Install packages and create variables

1. Create project folder, and CD into it.
1. Init pipenv, and install packages: `pipenv install --python "$PYENV_ROOT/shims/python" psycopg2-binary Flask-SQLAlchemy alembic Flask-Migrate Flask python-dotenv`
1. Create `.env` or `.flaskenv` file, and add these variables:
```
FLASK_APP=flask_migrate_test.py
FLASK_ENV=development
DATABASE_URL=postgresql://flask_migrate_test:flask_migrate_test@localhost/flask_migrate_test
```

# Create files

Create these and populate them:
- `app/`
- `app/__init__.py`
- `app/models.py`
- `flask_migrate_test.py` This is the entry file

# Create A Migration

1. Run `pipenv run flask db init`
    - This creates a new migrations folder where Alembic migrations will be created.
1. Add the first model to `app/models.py`
1. Create migration: `pipenv run flask db migrate -m "create owners table"`

This should create a new migration file `migrations/versions/..._create_owners_table.py`. It includes completed `upgrade()` and `downgrade()` methods.

4. If it all looks correct, apply the migration: `pipenv run flask db upgrade`
 
 There should now be a new `owners` table in the database.

# View Alembic Commands

Run: `pipenv run flask db --help`
