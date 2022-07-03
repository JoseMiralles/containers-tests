# Setup

1. Open psql: `sudo -u postgres psql`
1. Create user: `CREATE USER alembic_test WITH PASSWORD 'alembic_test';`
1. Create database: `CREATE DATABASE alembic_test WITH OWNER alembic_test;`
1. Create Pipenv: `pipenv install --python "$PYENV_ROOT/shims/python"`
1. Install Alembic: `pipenv install alembic psycopg2-binary`
    - Fact: Alembic includes an executable in `.venv/bin`

# Configure Enviroment

1. CD into the project folder.
1. Start pipenv shell: `pipenv shell`
1. `pipenv run alembic init <directory-name>`
    - Most people use `alembic` as the directory-name.
    - This will create a new directory where migrations will be defined and created.
1. Open `<directory-name>.ini`, which would be `alembic.ini` for most people.
    1. Uncoment and modify `file_template` to display a friendlier value.

```
file_template = %%(year)d%%(month).2d%%(day).2d_%%(hour).2d%%(minute).2d%%(second).2d_%%(slug)s
```
5. Open `alembic/env.py`, add `import os` at the top, and then add the following before the definition of `run_migrations_offline()`:

```
config.set_main_option("sqlalchemy.url", os.environ.get("DATABASE_URL"))

def run_migrations_offline() -> None:
    ...
```
6. Create db url enviroment variable: `export DATABASE_URL=postgresql://alembic_test:alembic_test@localhost/alembic_test`
    - Can be done using .flaskenv file instead as well. Remember to not include `export `

# Creating and applying migrations

1. Create migration: `pipenv run alembic revision -m "create the owners table"`
    - This creates `alembic/versions/6a4505dea246_create_the_owners_table.py`
1. Use the `def upgrade()` to define the changes to be applied to the database by this migration. And use `def downgrade()` to define the changes necessary to undo this migration.

```
def upgrade() -> None:
    op.create_table(
        "owners",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String(50), nullable=False),
        sa.Column("last_name", sa.String(50), nullable=False),
        sa.Column("email", sa.String(255), nullable=False)
    )


def downgrade() -> None:
    op.drop_table()
```
3. Apply migrations: `pipenv run alembic upgrade <revision>`
    - Replace `<revision>` with one of these:
        - `head`: Apply all un-applied revisions.
        - `+n`: Run n number of revisions from the currently applied revision.
        - `<Revision ID>`: The specific revision id, which is in the file.

# View History

Use `pipenv run alembic history` to view all the applied migrations.

# Downgrade / Rollback

Use `alembic downgrade <revision>`
    - Replace `<revision>` with one of these:
        - `base`: Rollback all revisions.
        - `-n`: Rollback -n number of revisions from the current one.
        - `<Revision ID>`

# Alembic Merge

Each revision has a `down_revision` value which points to the revision ID of the previous revision. But if two team members create revisions in their own git branches, and then these are both merged into main. Then the next person to try to apply all the revisions will get the following error:

```
FAILED: Multiple head revisions are present for given argument 'head';
please specify a specific target revision, '<branchname>@head' to
narrow to a specific head, or 'heads' for all heads
```

To fix this, the revisions need to be merged as described here: https://alembic.sqlalchemy.org/en/latest/branches.html
