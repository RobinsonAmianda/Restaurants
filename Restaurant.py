class Restaurant:
    def __init__(self):
        return None
    def get_Restaurant_name(self):
        print(self)
    def set_Restaurant_name(self,name):
        self._name = name
        if name == "Viilla Rossa Kempinski":
            print(f"Restaurant name: {self._name}")
        else:
            print(f"{name} is not the restaurant name")
    name = property(get_Restaurant_name,set_Restaurant_name)

R1 = Restaurant()
R1.set_Restaurant_name("Viilla Rossa Kempinski")



