import random


class Database:
    __instance = None

    def __init__(self):
        self.id = random.randint(1, 10000)
        print(f"loading database...")

    def __str__(self):
        return f"id: {self.id}"

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance


if __name__ == "__main__":
    d1 = Database()
    print(d1)
    d2 = Database()
    print(d2)
    print(d1 == d2)
