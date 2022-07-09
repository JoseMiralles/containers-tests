This is a library that allows us to interface with a Postgresql database.

# Setup

## Install package, create and populate database.

1. Install package: `pipenv install psycopg2-binary`
1. Create `db.sql`
1. Open psql: `sudo -u postgres psql`
1. Create user: `CREATE USER psycopg_test_user WITH CREATEDB PASSWORD 'password';`
    - This shouldnt be done in a real world application!
1. Create db: `CREATE DATABASE psycopg_test_db WITH OWNER psycopg_test_user;`
1. Exit psql by pressing `ctrl + z`
1. Create a sql file `touch db.sql` and then add your create table and insert into commands. Look at the example file below.
1. Execute: `sudo -u postgres psql -U psycopg_test_user -d psycopg_test_db -f db.sql -h localhost`
    - This populates the `psycopg_test_db` database, and sets the `psycopg_test_user` as the owner of the new tables.

Example `db.sql`
```
CREATE TABLE owners (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);

-- Make and model should have their own tables
-- Simplified for now
CREATE TABLE cars (
  id SERIAL PRIMARY KEY,
  manu_year INTEGER NOT NULL,
  make VARCHAR(255),
  model VARCHAR(255),
  owner_id INTEGER NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES owners(id)
);

INSERT INTO owners (first_name, last_name, email)
VALUES
('Tim', 'Petrol', 'rotary@fast.com'),
('Ryan', 'Runner', '10sec@jdm.com'),
('Tia', 'Petrol', 'typer@wtec.com');

INSERT INTO cars (manu_year, make, model, owner_id)
VALUES
(1993, 'Mazda', 'Rx7', 1),
(1995, 'Mitsubishi', 'Eclipse', 2),
(1994, 'Acura', 'Integra', 3);
```

<br>

# Connect to RDBMS using Psycopg

## Conversions


| PostgreSQL |	Python |
|-|-|
| NULL |	None |
| bool |	bool |
| double |	float |
| integer |	long |
| varchar |	str |
| text |	unicode |
| date |	date |


## Example Repository

```
from typing import Tuple, List
import psycopg2

CONNECTION_PARAMETERS = {
    'dbname': 'psycopg_test_db',
    'user': 'psycopg_test_user',
    'password': 'password',
    'host': 'localhost',
}

class GarageRepository:

    @staticmethod
    def get_all_cars() -> List[Tuple[str,str,str,str]]:
        with psycopg2.connect(**CONNECTION_PARAMETERS) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT manu_year, make, model, owner_id from cars;")
                return cursor.fetchall()

    @staticmethod
    def get_cars_by_user_id(user_id: int) -> List[Tuple[str,str,str]]:
        """
        Get's the cars owned by the specified user.
        """
        with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
            with conn.cursor() as cursor:
                owner_id = 1
                cursor.execute("""
                    SELECT manu_year, make, model FROM cars
                    WHERE owner_id = %(owner_id)s
                """,
                {"owner_id": owner_id})
                return cursor.fetchall()

    @staticmethod
    def add_new_car(year: int, make: str, model: str, owner_id: int) -> None:
        with psycopg2.connect(**CONNECTION_PARAMETERS) as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO cars (manu_year, make, model, owner_id)
                    VALUES (%(manu_year)s, %(make)s, %(model)s, %(owner_id)s)
                """,
                {
                    "manu_year": year,
                    "make": make,
                    "model": model,
                    "owner_id": owner_id
                })

    @staticmethod
    def change_car_owner(car_id: int, new_owner_id: int) -> None:
        with psycopg2.connect(**CONNECTION_PARAMETERS) as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE cars SET owner_id = %(new_owner_id)s
                    WHERE id = %(car_id)s
                """,
                {
                    "car_id": car_id,
                    "new_owner_id": new_owner_id
                })


print(GarageRepository.get_all_cars())
GarageRepository.add_new_car(year=1991, make="Honda", model="Civic", owner_id=2)
print(GarageRepository.get_all_cars())
GarageRepository.change_car_owner(0, 2)
print(GarageRepository.get_all_cars())

```

