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
    def all_names(self,):
        print(f"{self.given_name} {self.family_name}")
       
class Restaurants():
    def __init__(self,name):
        self.name = name
    def customer_restaurants(self):
        if self.name == "Villa Rossa Kempinski":
            print(f"Restaurants visited: {self.name}")
        else:
            print(f"{self.name} was not visited by customer.")
    def customer_add_review(self,Restaurant,rating):
        self.Restaurant = Restaurant
        self.rating =int(rating)
        print(f"Restaurant: {self.Restaurant}")
        print(f"Rating: {self.rating}")
    def Customer_num_reviews(reviews):
        reviews = []
        for review in reviews:
            return review
    def Customer_find_by_name(name):
        full_name = [""]
        for name in full_name:
            if name == full_name:
                return name 

#Returning customer first and family name        
""" c1 = Customer("Robinson","Okusala")
c1.all_names() """
#Returning visited restaurants
""" c1 = Restaurants("Villa Rossa Kempinski")
c1.customer_restaurants() """
#Returning restaurant and its ratings
"""c1.customer_add_review("Villa Rossa Kempinski",5)"""

    
        