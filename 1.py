class Soda:
    def __init__(self,soda, dobavka= str(input())):
        self.soda = soda
        self.dobavka = dobavka
    def show_my_drink(self):
        if self.dobavka in self.soda:
            print(f"Soda with dobavka {self.dobavka}")
        else:
            print("Soda without dobavka")
soda = Soda("Soda")
print(soda)
