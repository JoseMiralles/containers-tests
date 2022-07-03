 # Instalation

Psycopg is required by SQLAlchemy

1. Install postgresql-common in not yet installed: `sudo apt install postgresql-common` 
1. Install packages: `pipenv install psycopg2-binary sqlalchemy --python "$PYENV_ROOT/shims/python"`

<br>

# Setup database

1. Open psql: `sudo -u postgres psql`
1. Create user: `CREATE USER sqlalchemy_test WITH CREATEDB PASSWORD 'password';`
1. Create database: `CREATE DATABASE sqlalchemy_test WITH OWNER sqlalchemy_test;`
1. Exit out of psql, and create `db.sql`:
```
CREATE TABLE owners (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);

CREATE TABLE ponies (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  birth_year INTEGER NOT NULL,
  breed VARCHAR(255),
  owner_id INTEGER NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES owners(id)
);

CREATE TABLE handlers (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  employee_id VARCHAR(12) NOT NULL
);

CREATE TABLE pony_handlers (
  pony_id INTEGER NOT NULL,
  handler_id INTEGER NOT NULL,
  PRIMARY KEY (pony_id, handler_id),
  FOREIGN KEY (pony_id) REFERENCES ponies(id),
  FOREIGN KEY (handler_id) REFERENCES handlers(id)
);

INSERT INTO owners (first_name, last_name, email)
VALUES
('Joey', 'Harker', 'joey@harker.edu'),
('Jay', 'Harker', 'jay@harker.edu'),
('Josetta', 'Harker', 'josetta@harker.edu');

INSERT INTO ponies (name, birth_year, breed, owner_id)
VALUES
('Lucky Loser', 2017, 'Halfinger', 2),
('Unlucky Usurper', 2012, 'Fleuve', 1),
('Impassive Emperor', 2016, 'Hirzai', 1);

INSERT INTO handlers (first_name, last_name, employee_id)
VALUES
('Zap', 'Branagan', 'O4F'),
('The', 'Crushinator', '00100010'),
('Bubblegum', 'Tate', 'bball117');

INSERT INTO pony_handlers (pony_id, handler_id)
VALUES
(1, 1),
(1, 2),
(2, 2),
(3, 1),
(3, 3);
```

- Notice `PRIMARY KEY (pony_id, handler_id),` in the pony_handlers table.

5. Run the sql script: `sudo -u postgres -psql -f db.sql -U sqlalchemy_test -d sqlalchemy_test -h localhost`

<br>

# Connecting SQLAlchemy to PostgreSQL

You need to define the URL in the following format:

```
  foo://example.com:8042/over/there?name=ferret#nose
  \_/   \______________/\_________/ \_________/\___/
   |           |            |            |       |
scheme     authority       path        query  fragment
```

For the example above, this would be the URL: ```postgresql://sqlalchemy_test:password@localhost/sqlalchemy_test```

`main.py`
```
from sqlalchemy import create_engine

CONNECTION_STRING = "postgresql://sqlalchemy_test:password@localhost/sqlalchemy_test"
engine = create_engine(CONNECTION_STRING)

with engine.connect() as connection:
    result = connection.execute("""
        SELECT o.first_name, o.last_name, p.name
        FROM owners o
        JOIN ponies p ON (o.id = p.owner_id)
    """)
    for row in result:
        print(row["first_name"], row["last_name"], "owns", row["name"])

# Always dispose of the engine.
engine.dispose()
```

<br>

# Creating Mappings / Models

`SQLAlchemy_project/model.py`
```
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.schema import Column, Table
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


# Many to many relationship
pony_handlers = Table(
    "pony_handlers",
    Base.metadata,
    Column("pony_id", ForeignKey("ponies.id"), primary_key=True),
    Column("handler_id", ForeignKey("handler.id"), primary_key=True)
)


class Owner(Base):
    __tablename__ = "owners"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))

    ponies = relationship(
        "Pony",
        back_populates="owner",
        cascade="all, delete-orphan" # delete ponies if they are owned only by this owner.
    )


class Pony(Base):
    __tablename__ = "ponies"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    birth_year = Column(Integer)
    breed = Column(String(255))
    owner_id = Column(Integer, ForeignKey("owners.id"))

    owner = relationship("Owner", back_populates="ponies")
    handlers = relationship( # Many to many using pony_handlers table
        "Handler",
        secondary=pony_handlers,
        back_populates="ponies")
```

<br>

# Adding Data to the database

```
new_owner = Owner(
    first_name="Luchentio",
    last_name="Fanucci",
    email="luchentio@aol.com"
)

new_pony = Pony(
    name="Buttercup",
    birth_date=2020,
    breed="Unicorn",
    owner=new_owner
)

CONNECTION_STRING = "postgresql://sqlalchemy_test:password@localhost/sqlalchemy_test"
engine = create_engine(CONNECTION_STRING)
SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()

session.add(new_owner)
session.commit()
# SQLAlchemy knows that new_pony is new even if it wasnt added to the session.

# Id's exist after commiting.
print(new_owner.id)
print(new_pony.id)
```

# Deleting
```
session.delete(pony)
sesison.commit()
```

# Querying
```
all_ponies_by_birth = session.query(Pony).order_by(Pony.birth_year)
one_pony = session.query(Pony).get(2) # By id
one_owner = session.query(Owner.first_name, Owner.last_name)
owners_with_u_in_name = session.query(Owner).filter(Owner.name.like("%u%"))

print(all_ponies_by_birth) # Prints the SQL query string.

# Perform fetch
ponies_result = all_ponies_by_birth.all()
for pony in ponies_result:
    print(pony.name)

# Can query with
#   all()           -> Get all records
#   first()         -> Get first
#   one()           -> Get one, or throw an error if 0 or more than 2 records exist.
#   one_or_none()   -> Get one, or none. Throw error if more than one exist.
#   count()         -> Total number of records.

# Query joins
hirzai_owners = session.query(Owner) \
                    .join(Pony) \
                    .filter(Pony.breed == "Hirzai")

# Eager loading (Solve N + 1 problem)
## This can be done with joinedload()
owners_and_ponies = session.query(Owner).options(joinedload(Owner.ponies))
for owner in owners_and_ponies:
    print(owner.first_name, owner.last_name)
    for pony in owner.ponies:
        print("\t", pony.name)

# Joining is possible as well, which would allow for pony filtering.
hirzai_owners_and_ponies = session.query(Owner) \
                                  .join(Pony)  \
                                  .filter(Pony.breed == "Hirzai") \
                                  .options(joinedload(Owner.ponies))
```
