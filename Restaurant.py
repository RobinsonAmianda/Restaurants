from Customer import Customer

class Restaurant():
    
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
    def all_reviews(self,customer,restaurant,rating):
         self.customer = customer
         self.restaurant = restaurant
         self.rating = rating
         print(f"Customer: {self.customer}")
         print(f"Restaurant: {self.restaurant}")
         print(f"Ratings: {self.rating} star(s)")
    name = property(get_Restaurant_name,set_Restaurant_name)

    def decorator(func):
        return func
    def Restaurant_average_star_rating(rating):
        total_sum = rating[0]
        return lambda total_sum,rating:(total_sum + rating) / len(rating)
    decorator(Restaurant_average_star_rating)
            
#Returning list of reviews
""" R1 = Restaurant()
R1.all_reviews("Robinson","Villa Rossa Kempinski",5) """

#Returning list of customers
""" R1 = Customer("Robinson","Amianda")
R1.all_names() """



