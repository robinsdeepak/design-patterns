from abc import ABC, abstractmethod
from enum import auto, Enum


class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This tea is delicious!")


class Coffee(HotDrink):
    def consume(self):
        print("This Coffee is delicious!")


class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Preparing Tea {amount} ml.")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Preparing Coffee {amount} ml.")
        return Coffee()


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = 1
        TEA = 2

    def get_factory_instance(self, idx):
        name = self.AvailableDrink(idx).name
        factory_name = name.title() + "Factory"
        return eval(factory_name)()

    def make_drink(self):
        print("Available drinks:")
        for d in self.AvailableDrink:
            print(f"{d.value}: {d.name}")

        s = input("Please pick a drink(ex: 1): ")
        drink_idx = int(s.strip())
        s = input("Specify Amount: ")
        amount = int(s)

        factory = self.get_factory_instance(drink_idx)
        return factory.prepare(amount)


if __name__ == "__main__":
    machine = HotDrinkMachine()
    drink = machine.make_drink()
    drink.consume()
