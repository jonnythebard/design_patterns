class Person:
    def __init__(self):
        self.address = None
        self.postcode = None
        self.city = None
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f'{self.address}, {self.postcode}, {self.city}, ' \
               f'{self.company_name}, {self.postcode}, {self.annual_income}'


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        # continue working on the person
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        # continue working on the person
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, address):
        self.person.address = address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


if __name__ == '__main__':
    person = PersonBuilder()
    jonny = person.works.at('restaurant').as_a('waiter').earning('9999') \
                        .lives.at('korea').with_postcode('1004').in_city('seoul') \
                        .build()
    print(jonny)

    peter = person.works.at('swimming pool').as_a('teacher').earning('10000') \
                        .lives.at('korea').with_postcode('1005').in_city('seoul') \
                        .build()
    print(peter)
