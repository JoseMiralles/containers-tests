from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.schema import Column, Table
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, joinedload

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


# Adding data

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


# Querying

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

session.close()
session.dispose()