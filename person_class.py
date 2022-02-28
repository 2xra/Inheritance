class Person:
    def __init__(self, name, address, phone):
        self._name = name
        self._address = address
        self._phone = phone

    def PrintPerson(self):
        print("name: ", self._name)
        print("address:", self._address)
        print("phone:", self._phone)


class Customer(Person):
    def __init__(self, name, address, phone, customernum, mail):
        Person.__init__(self, name, address, phone)
        self._custnum = customernum
        self._mail = mail

    def PrintPerson(self):
        print("name: ", self._name)
        print("address:", self._address)
        print("phone:", self._phone)
        print("customer number:", self._custnum.__str__())
        print("Mailing list:", self._mail)
