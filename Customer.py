class Customer:
    def __init__(self,given_name,family_name):
        self.given_name = given_name
        self.family_name = family_name
    def first_name(self):
        print(f"{self.given_name}")
    def last_name(self):
        print(f"{self.family_name}")
    def full_names(self):
        print(f"{self.given_name} {self.family_name}")
    def all_names(self):
        print(f"Given name: {self.given_name}")
        print(f"Family name: {self.family_name}")

c1 = Customer("Robinson","Amianda")
c1.all_names()

    
        