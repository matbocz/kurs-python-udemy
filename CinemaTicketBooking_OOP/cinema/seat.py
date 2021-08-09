import sqlite3


class Seat:
    """Represents a cinema seat that can be taken from a user"""

    database = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        """Get the price of a certain seat"""

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "price" FROM "Seat" WHERE "seat_id" = ?
        """, [self.seat_id])
        price = cursor.fetchall()[0][0]

        return price

    def is_free(self):
        """Check in the database if a seat is taken or not"""

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "taken" FROM "Seat" WHERE "seat_id" = ?
        """, [self.seat_id])
        result = cursor.fetchall()[0][0]

        if result == 0:
            return True
        else:
            return False

    def occupy(self):
        """Change value of taken in the database from 0 to 1 if seat is free"""

        if self.is_free():
            connection = sqlite3.connect(self.database)
            connection.execute("""
            UPDATE "Seat" SET "taken" = ? WHERE "seat_id" = ?
            """, [1, self.seat_id])
            connection.commit()
            connection.close()
