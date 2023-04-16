import mysql.connector
from models.product import Product
from typing import List
ProductList = List[Product]

mydb = mysql.connector.connect(
    host="103.168.56.144",
    user="mnmonherdene_admin",
    password="MnMonherdene0529?",
    database="python_sql"
)


def insert_product(product: Product) -> bool:
    cursor = mydb.cursor()

    sql = f"INSERT INTO product (name, info, price) VALUES ('{product.name}', '{product.info}', {product.price})"
    cursor.execute(sql)

    mydb.commit()

    if cursor.rowcount > 0:
        return True
    else:
        return False


def select_products() -> ProductList:
    cursor = mydb.cursor()

    sql = f"SELECT * FROM product"
    cursor.execute(sql)

    result = cursor.fetchall()

    products: ProductList = []

    for x in result:
        products.append(Product(x[0], x[1], x[2], x[3], x[4], x[5]))

    return products


def delete_product(product_id: int) -> bool:
    cursor = mydb.cursor()

    select_sql = f"SELECT * FROM product WHERE id={product_id}"
    cursor.execute(select_sql)

    result = cursor.fetchone()

    if result is None:
        return False

    delete_sql = f"DELETE FROM product WHERE id={product_id}"
    cursor.execute(delete_sql)

    mydb.commit()

    if cursor.rowcount > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    delete_product(1)
