class Review:
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

p1 = Review("Robinson Okusala","Villa Rossa Kempinski",5)
p1.all()

