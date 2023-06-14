class CEO:
    __shared_state = {
        'name': 'John',
        'since': 2016
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f"{self.name} is CEO since {self.since}"


if __name__ == "__main__":
    ceo1 = CEO()
    print('ceo1: ', ceo1)

    ceo2 = CEO()
    print('ceo2: ', ceo2)

    print('updating ceo2')
    ceo2.name = 'doe'
    ceo2.since = 2018
    print('ceo1: ', ceo1)
    print('ceo2: ', ceo2)
