#%%
alien_0 = {'color':'green', 'points':5}

print(alien_0['color'])
print(alien_0['points'])



# %%
alien_0['x_points'] = 0
alien_0['y_points'] = 25
print(alien_0) 


# %%
alien_1 = {}
alien_1['color']='red'
print(alien_1)


# %%
print(alien_0)
del alien_0['color']
print(alien_0)


# %%
favorite_languages={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil':'python'
}
print(favorite_languages['jen'])

# %%
david={
    'first_name' : 'atony',
    'last_name' :'david',
    'age':23,
    'city':'LA'
}
print(david)
# %%
favorite_numbers={
    'alice':11,
    'bob':22,
    'carile':23,
    'david':13,
    'estar':0
}
print(favorite_numbers)


# %%
user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}

# %%
for key,value in user_0.items():
    print("\nKey: "+key)
    print("Value: "+value)


# %%
print(user_0.items())


# %%
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is"+
        language.title()+"." )
# %%
for name in favorite_languages.keys():
    print(name.title())
# %%
for name in favorite_languages:
    print(name)
# %%
favorite_languages={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil':'python'
}
if 'evil' not in favorite_languages.keys():
    print("evil, you are not in here")
# %%
if 'evil' not in favorite_languages.keys():
    print("evil, you are not in here")

# %%
for name in sorted(favorite_languages.keys()):
    print(name.title())

# %%
for language in favorite_languages.values():
    print(language.title())


# %%
for language in set(favorite_languages.values()):
    print(language.title())



# %%
rivers={
    'nile':'egypt',
    'LongRiver':'China',
    'YellowRiver':'China',
}
for river,county in rivers.items():
    print("The "+river+" runs through "+county+".")

# %%
for river in rivers.keys():
    print(river.title())

# %%
for country in rivers.values():
    print(country)


# %%
alien_0['color']
# %%
alien_0={'color': 'green', 'points': 5}
alien_1={'color': 'red', 'points': 6}
alien_2={'color': 'yellow', 'points':15 }
aliens=[alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# %%
aliens = []
for number in range(30):
    new_alien = {'color':'green', 'points':number, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")
print("total aliens : "+str(len(aliens)))


# %%
pizza={
    'crust':'thick',
    'toppings':['mushroom','extra cheese']
}
for topping in pizza['toppings']:
    print(topping)


# %%
favorite_languages={
    'jen':['py','C'],
    'sarah':['C'],
    'edward':['ruby','go']
}
for name,languages in favorite_languages.items():
    print("\n"+name.title()+"'s favorite language are:")
    for language in languages:
        print("\t"+language.title())


# %%
bob={'name':'bob' ,'age':12}
tom={'name':'tom','age':13}
people = [bob,tom]
for value in people:
    print(value['name']+"\t"+str(value['age']))


# %%
cat={'name':'tom', 'age':3}
dog={'name':'jack', 'age':5}
fish={"name":'Bob', 'age':2}
pets=[cat,dog,fish]
for pet in pets:
    print(pet['name']+" "+str(pet['age']))


# %%
favorite_places={
    'jack':['beijing','shanghai'],
    'tom':['shandong'],
    'jerry':['hainan']
}
for name,places in favorite_places.items():
    print(name+"'s favorite places are:")
    for place in places:
        print("\tplace")

# %%
cities={
    'beijing':{
        'country':'china',
        'people':"1.5 billion",
        'history':'history'
    },
    'shanghai':{
        'country':'china',
        'people':"1.5 billion",
        'history':'history'
    },
    'chongqing':{
        'country':'china',
        'people':"1.5 billion",
        'history':'history'
    }
}
for city,infos in cities.items():
    print(city+ " info:")
    print("\tcountry : "+infos['country']+
        "\n\tpeople : "+infos['people']+
        "\n\thistory: "+infos['history']
    )


# %%
