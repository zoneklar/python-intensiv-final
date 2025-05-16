import sqlite3


def create_product_table(cursor, connection):
    sql = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price INTEGER NOT NULL
        );
        """
    cursor.execute(sql)
    connection.commit()


def insert_products(cursor, connection, products):
    sql = "INSERT INTO products (name, price) VALUES (?, ?)"
    cursor.executemany(sql, products)
    connection.commit()


def read_products(cursor: sqlite3.Cursor) -> list:
    """Lese Produkt aus Produkttable."""
    sql = "Select * from products"
    cursor.execute(sql)
    products = cursor.fetchall()
    return products


def read_product(cursor: sqlite3.Cursor, id_: int) -> tuple:
    sql = "Select * from products WHERE id=?"
    cursor.execute(sql, (id_,))
    product = cursor.fetchone()
    if product is not None:
        return product
    else:
        raise ValueError("Das Objekt ist nicht vorhanden.")


if __name__ == "__main__":
    with sqlite3.connect("job.db") as connection:
        cursor = connection.cursor()
        create_product_table(cursor, connection)

        products = [
            ("Milka", 190),
            ("Lego Set", 290),
            ("Race car", 1190),
        ]
        # Produkte in Datenbank übertragen
        insert_products(cursor, connection, products)

        # Daten auslesen
        products = read_products(cursor)
        print(products)

        # Ein Produkt auslesen
        product = read_product(cursor, 3)
        print(product)
