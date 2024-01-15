import dataclasses


@dataclasses.dataclass
class User:
    name: str
    email: str
    password: str

