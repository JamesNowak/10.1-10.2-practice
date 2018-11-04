class Data:  # sets the structure of the program
    def __init__(self, name, address, age, phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone


def main():
    d1 = Data("James", "5301, Woodland Dr.", 18, "815-451-1412")  # My fake data
    d2 = Data("Billie", "4505, Turncoat Ln.", 37, "815-456-7690")  # mothers dake data
    d3 = Data("Anthony", "3067, Elm Rd", 47, "345-9078-5639")  # Fathers fake data

    print(d1.name)  # This block prints my info
    print(d1.address)
    print(d1.age)
    print(d1.phone)

    print("-------------")

    print(d2.name)  # this block prints my mothers info
    print(d2.address)
    print(d2.age)
    print(d2.phone)

    print("-------------")

    print(d3.name)  # this block prints my fathers info
    print(d3.address)
    print(d3.age)
    print(d3.phone)


main()
