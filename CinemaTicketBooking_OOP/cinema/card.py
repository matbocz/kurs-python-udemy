import sqlite3


class Card:
    """Represents a bank card needed to finalize a seat purchase"""

    database = "banking.db"

    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        """Checks if card is valid and has balance. Subtracts price from balance"""

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "balance" FROM "Card" WHERE "number" = ? AND "cvc" = ?
        """, [self.number, self.cvc])
        result = cursor.fetchall()

        if result:
            balance = result[0][0]
            if balance >= price:
                connection.execute("""
                UPDATE "Card" SET "balance" = ? WHERE "number" = ? AND "cvc" = ?
                """, [balance - price, self.number, self.cvc])
                connection.commit()
                connection.close()

                return True
