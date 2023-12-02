from Restaurant import Restaurant
from Customer import Customer
class Review(Customer,Restaurant):
    def __init__(self,customer,restaurant,rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
    def ratings(self):
        print(f"{self.rating} star(s)")
    def all(self):
        print(f"Customer: {self.customer}")
        print(f"Restaurant: {self.restaurant}")
        print(f"Ratings: {self.rating} star(s)")
    def review_customer(self):
        return super().all_names()
    def review_restaurant(self):
        return super().set_Restaurant_name()
    
#Returns restaurant info        
""" R1 = Restaurant()
R1.set_Restaurant_name("Viilla Rossa Kempinski") """
#Returns customers list
""" c1 = Customer("Robinson","Okusala")
c1.all_names() """ 
#Returning all reviews
""" p1 = Review("Robinson Okusala","Villa Rossa Kempinski",5)
p1.all() """


