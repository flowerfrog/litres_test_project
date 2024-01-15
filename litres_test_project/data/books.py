import dataclasses


@dataclasses.dataclass
class Book:
    name: str
    author: str
    price: str
    url: str
