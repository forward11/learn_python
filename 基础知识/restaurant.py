class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print("the restaurant's name is "+self.restaurant_name.title())
        print("the cuisine's type is "+self.cuisine_type)

    def open_restaurant(self):
        print("the restaurant is open")

    def increment_number_served(self,add):
        self.number_served +=add