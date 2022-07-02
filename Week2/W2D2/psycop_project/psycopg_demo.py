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
