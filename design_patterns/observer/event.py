class Event(list):
    def __call__(self, *args, **kwargs):
        for subscriber in self:
            subscriber(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        # invoke subscribers
        self.falls_ill(self.name, self.address)


def report(name, address):
    # subscriber
    print(f'{name} is ill')


def call_doctor(name, address):
    # subscriber
    print(f'A doctor has been called to {address}')


if __name__ == '__main__':
    person = Person('Sherlock', '221B Baker St')

    # add subscribers to catch_a_cold method
    person.falls_ill.append(report)
    person.falls_ill.append(call_doctor)

    # subscribers are called
    person.catch_a_cold()

    # and you can remove subscriptions too
    person.falls_ill.remove(call_doctor)
    person.catch_a_cold()
