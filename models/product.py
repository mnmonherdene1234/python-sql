from datetime import datetime


class Product:
    def __init__(self, id: int = 0, name: str = "", info: str = "", price: int = 0, created_at: datetime = datetime.now(), updated_at: datetime = datetime.now()) -> None:
        self.id = id
        self.name = name
        self.info = info
        self.price = price
        self.created_at = created_at
        self.updated_at = updated_at
