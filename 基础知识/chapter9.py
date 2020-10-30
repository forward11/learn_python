#%%
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def sit(self):
        print(self.name.title()+" is now sitting.")
    
    def roll_over(self):
        print(self.name.title()+ " rolled over!")
# %%
my_dog = Dog('willie',6)
print("my dog's name is "+my_dog.name.title())
print("his age is "+str(my_dog.age))


# %%
my_dog.sit()
my_dog.roll_over()





# %%
class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
    def describe_user(self):
        print("his name is "+self.first_name+" "+self.last_name)
    def greet_user(self):
        print("hello! "+self.first_name)
    def increment_login_attempts(self):
        self.login_attempts +=1
    def reset_login_attempts(self):
        self.login_attempts=0

user=User('james','harden')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)




# %%
my_new_car.update_odometer(25)
my_new_car.read_odometer()



# %%
class Car():
    """simulation car"""
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make +' '+self.model
        return long_name.title() 

    def read_odometer(self):
        print("this car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        self.odometer_reading= mileage
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-KWh battery.")


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-KWH battery.")
    

my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()





#%%     9-6
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



class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)  
        self.flavors=['a-flavor','b-flavor']      

    def show_flavors(self):
        print(self.flavors)

restaurant=IceCreamStand('KFC','CHICKEN')
restaurant.show_flavors()






# %%
class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges=Privileges()
    

class Privileges():
    def __init__(self):
        self.privileges=["can add post","can delete post","can ban user"]

    def show_privileges(self):
        print(self.privileges)


admin =Admin('james','harden')
admin.privileges.show_privileges()





# %%
from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen']='python'
favorite_languages['sarah']='c'
favorite_languages['edward']='ruby'
favorite_languages['phil']='python'

for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+
            language.title()+".")

print(favorite_languages)





# %%
from random import randint

class Die():
    def __init__(self,sides=6):
        self.sides=sides
    
    def roll_doe(self):
        print(randint(1,self.sides))

die=Die()
for i in range(1,11):
    die.roll_doe()
print("\n\n")

die_10=Die(10)
for i in range(1,11):
    die_10.roll_doe()
print("\n\n")

die_20=Die(20)
for i in range(1,11):
    die_20.roll_doe()
print("\n\n")






