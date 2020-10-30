#%%
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)

# %%
print(bicycles[2].title())
print(bicycles[-1])
print(bicycles[-2])

# %%
names=['ming','uzi','xiaohu','zoom','doinb']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
message='hello! '+ names[0]+" !"
print(message)


# %%
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)



#%%
print(motorcycles)
del motorcycles[0]
print(motorcycles)


#%%
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('suzuki')
print(motorcycles)


# %%
people=['Alice','Bob','cat','davis']
print(people[1]+" can't be here.")
people[1]='baby'
print(people)

people.append("err")
people.append("fuck")
people.append("gigi")
print(people)
people.insert(0,'jordan')
print(people)

# %%
print(people)

# %%
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)


# %%
cars.sort(reverse=True)
print(cars)


# %%
cars=['bmw','audi','toyota','subaru']
print(cars)
print(sorted(cars))
print(cars)

# %%
print(sorted(cars))
print(sorted(cars,reverse=True))


# %%
print(cars)
cars.reverse()
print(cars)


# %%
places=['LA','NY','Tibet','UK','France']
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)


# %%
places.reverse()
print(places)
places.reverse()
print(places)


# %%
places.sort()
print(places)
places.sort(reverse=True)
print(places)



# %%
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician.title()+", that was a great trick!")
    print("I can't wait to see your next trick, "+magician.title()+".\n")
print("Thank you, everyone!")



# %%
message="hello"
print(message)



# %%
for magician in magicians:
    print(magician)


# %%
for value in range(1,6):
    print(value)


# %%
numbers=list(range(1,6))
print(numbers)


# %%
even_numbers=list(range(2,12,2))
even_numbers


# %%
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)


# %%
digits=list(range(0,10))
print(min(digits))
print(max(digits)) 
print(sum(digits))


# %%
squares=[value**2 for value in range(1,11)]
print(squares)



# %%
number_list=[value for value in range(1,1000001)]
print(min(number_list))
print(max(number_list))
print(sum(number_list))


# %%
odd_list=[value for value in range(1,20,2)]
for value in odd_list:
    print(value)


# %%
div3_list=[value for value in range(3,31,3)]
for value in div3_list:
    print(value)


# %%
cube_list=[value**3 for value in range(1,11)] 
print(cube_list)


# %%
players=['charles','martina','michael','florence','eli']
print(players[0:3])



# %%
for player in players[:3]:
    print(player.title())


# %%
my_foods=['pizza','falafel','carrot cake','apple']
friend_foods=my_foods[:]
print(friend_foods)


# %%
print(my_foods[:3])
print(my_foods[-3:])


# %%
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])


# %%
for dimension in dimensions:
    print(dimension)



# %%
foods=('pizza','apple','banana','pear','peach')
for food in foods:
    print(food)
foods=('pizza','apple','banana','bear','tiger')
for food in foods:
    print(food)


