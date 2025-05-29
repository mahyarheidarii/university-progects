class Human:
    def __init__(self, national_id, name, role):
        self.national_id = national_id
        self.name = name
        self.role = role

    def leave(self):
        print(self.name + " requested leave.")

    def salary(self):
        if self.role in ["Manager", "Staff"]:
            print(self.name + " received salary.")
        else:
            print(self.name + " has no salary.")

    def working_hours(self):
        if self.role == "Manager":
            print(self.name + " works 9am to 5pm.")
        elif self.role == "Staff":
            print(self.name + " works 8am to 4pm.")
        else:
            print(self.name + " has no working hours.")

    def action(self):
        if self.role == "Manager":
            print(self.name + " is managing.")
        elif self.role == "Staff":
            print(self.name + " is working.")
        elif self.role == "Customer":
            print(self.name + " is ordering food.")

class Food:
    def __init__(self, name, price, cook_time, category):
        self.name = name
        self.price = price
        self.cook_time = cook_time
        self.category = category

    def taste(self):
        print(self.name + " tastes good.")

    def make_full(self):
        print(self.name + " makes you full.")

    def make_thirsty(self):
        print(self.name + " makes you thirsty.")


h1 = Human("123", "Ali", "Manager")
h2 = Human("456", "Sara", "Customer")
f1 = Food("Kebab", 200000, 30, "Iranian")

h1.action()
h2.salary()
f1.taste()
