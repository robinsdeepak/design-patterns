import random


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    __instance = None

    def __init__(self):
        self.id = random.randint(1, 10000)
        print(f'loading database...')

    def __str__(self):
        return f"id: {self.id}"


if __name__ == "__main__":
    d1 = Database()
    print(d1)
    d2 = Database()
    print(d2)
    print(d1 == d2)
