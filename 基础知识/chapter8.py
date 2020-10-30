#%%
def display_message(content):
    print("you are learing "+content+".")
display_message("function")
# %%
def faorite_book(title):
    print("One if my favorite books is "+title.title())
faorite_book("people")

# %%
def describe_pet(pet_name='ss',animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a "+animal_type +".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('harry','A')

# %%
def make_shirt(size='T', picture='I love Python'):
    print("your T-shirt's size is : "+size)
    print("your T-shirt's picture is : "+picture)
make_shirt()
make_shirt('M')
make_shirt('S','I love Java')


# %%
def describe_city(name,country='china'):
    print(name+" is in "+country)
describe_city('nanjing')
describe_city('beijing')
describe_city('Boston','USA')


# %%
def build_person(first_name,last_name):
    person={'first':first_name, 'last':last_name}
    return person

musician = build_person('jimi','hendrix')
print(musician)


# %%
def build_person(first_name,last_name,age=''):
    person={'first':first_name, 'last':last_name}
    if age:
        person['age']=age
    return person

musician = build_person('jimi','hendrix',12)
print(musician)

# %%
def make_album(singer_name, album_name):
    album = {'singer_name':singer_name, 'album_name':album_name}
    print("\nthe singer is "+singer_name)
    print("the album is "+album_name)
make_album('bruce','wind')
make_album('taylor','ray')
# %%
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians=['air','bone','car']
show_magicians(magicians)


# %%
def make_great(magicians):
    while magicians:
        current_magician ="the Great " + magicians.pop()
        complete_magicians.append(current_magician)
magicians=['air','bone','car']
complete_magicians=[]
make_great(magicians)
show_magicians(complete_magicians)
show_magicians(magicians)
# %%
magicians=['air','bone','car']
complete_magicians=[]
make_great(magicians[:])
show_magicians(complete_magicians)
show_magicians(magicians)


# %%
def make_pizza(*toppings):
    print(toppings)

make_pizza('mushroom','green peppers','extra cheese')

# %%
def build_car(manufacturer,model,**car_info):
    car={}
    car['manufacturer']=manufacturer
    car['model']=model
    for key,value in car_info.items():
        car[key]=value
    return car
user_car=build_car('subaru','outback',color='blue',two_package=True)
print(user_car)

# %%
import pizza
from pizza import make_big_pizza
from pizza import make_big_pizza as mbp
import pizza as p
from pizza import *
p.make_big_pizza(16,'pepperoni')