from data_access import select_products, insert_product, delete_product
from models.product import Product
from tabulate import tabulate

while True:
    print("0. Программаас гарах")
    print("1. Барааны жагсаалт харах")
    print("2. Бараа нэмж оруулах")
    print("3. Бараа устгах")

    try:
        user_input = int(input("\033[92m$:\033[0m"))
        if user_input == 0:
            break
        elif user_input == 1:
            products = select_products()

            headers = ["ID", "Нэр", "Тайлбар", "Үнэ", "Огноо"]
            rows = [[p.id, p.name, p.info, p.price, p.created_at]
                    for p in products]
            print(tabulate(rows, headers=headers))
        elif user_input == 2:
            name = input("\033[92mНэр: \033[0m")
            info = input("\033[92mТайлбар: \033[0m")

            price = ""

            while not isinstance(price, int):
                try:
                    price = int(input("\033[92mҮнэ: \033[0m"))
                except ValueError:
                    print("\033[91mҮнэ оруулна уу!\033[0m")

            product = Product(name=name, info=info, price=price)

            if insert_product(product):
                print("\033[92mАмжилттай\033[0m")
            else:
                print("\033[91mАмжилтгүй\033[0m")
        elif user_input == 3:
            id = ""

            while not isinstance(id, int):
                try:
                    id = int(
                        input("\033[92mУстгах барааны ID оруулна уу: \033[0m"))
                except ValueError:
                    print("\033[91mТоо оруулна уу!\033[0m")

            if delete_product(id):
                print("\033[92mАмжилттай\033[0m")
            else:
                print("\033[91mАмжилтгүй\033[0m")
        else:
            print("\033[93mЗөв тоо оруулна уу!\033[0m")
    except ValueError:
        print("\033[91mЗөвхөн тоо оруулна уу!\033[0m")
