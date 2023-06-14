import random


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):

    def __init__(self):
        self.id = random.randint(1000, 10000)
        print('loading database...')

    def __str__(self):
        return f"id: {self.id}"


if __name__ == "__main__":
    d1 = Database()
    print(d1)
    d2 = Database()
    print(d2)
    print(d1 == d2)

