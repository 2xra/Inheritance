class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def PrintPerson(self):
        print("name: ", self.__name)
        print("address:", self.__address)
        print("phone:", self.__phone)


class Customer(Person):
    def __init__(self, name, address, phone, customernum, mail):
        Person.__init__(self, name, address, phone)
        self.__custnum = customernum
        self.__mail = mail

    def PrintPerson(self):
        Person.PrintPerson(self)
        print("customer number:", self.__custnum.__str__())
        print("Mailing list:", self.__mail)
