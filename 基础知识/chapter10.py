#%%
file_name = 'pi_digits.txt'

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
    


# %%
file_name='pi_million_digits.txt'

with open(file_name) as file_object:
    lines=file_object.readlines()

pi_string=''
for line in lines:
    pi_string += line.strip()

birthday=input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("yes")
else:
    print("no")





#%%
file_name='learning_python.txt'

with open(file_name) as file_object:
    content=file_object.read()
    print(content)
print("\n")

with open(file_name) as file_object:
    for line in file_object:
        print(line.strip())
print("\n")

with open(file_name) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())
print("\n")



#%%
file_name='learning_python.txt'

with open(file_name) as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line.replace('Python','C'))




# %%
file_name='programing.txt'

with open(file_name,'w') as file_object:
    file_object.write("I love programing")


# %%
name = input("please input your name: ")
with open('guest.txt','a') as file_object:
    file_object.write(name)


# %%
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
print("continue...")



#%%
title="alice in wonderland "
title.split()


#%%
number_1=input("number 1 is : ")
number_2=input("number 2 is : ")
try:
    add=int(number_1)+int(number_2)
except ValueError:
    print("你输入的不是数字！")
else:
    print("the answer is "+str(add))



#%%
try:
    with open('cats.txt') as file_object:
        content=file_object.read()
        print(content)
except FileNotFoundError:
    pass
try:
    with open('dogs.txt') as file_object:
            content=file_object.read()
            print(content)
except FileExistsError:
    pass



#%%
import json

numbers=[2,3,5,7,11,13]

file_name='numbers.json'

with open(file_name,'w') as f_obj:
    json.dump(numbers,f_obj)

with open(file_name) as f_obj:
    numbers_read=json.load(f_obj)
print(numbers_read)


#%%
import json

username=input("What is your name?")

filename='username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll remember you when you come back, "+username+"!")



#%%
import json

filename='username.json'

with open(filename) as f_obj:
    username=json.load(f_obj)
    print(username)





#%%
favorite_number=input("input your favorite number: ")
filename='favorite_numbers.json'

with open(filename,'w') as f_obj:
    json.dump(favorite_number,f_obj)

with open(filename) as f_obj:
    number=json.load(f_obj)
    print("I know your favorite number is "+number) 


# %%
import json
filename='favorite_number.json'

try:
    with open(filename) as f_obj:
        number=json.load(f_obj)
except FileNotFoundError:
    favorite_number=input("input your favorite number: ")
    with open(filename,'w') as f_obj:
        json.dump(favorite_number,f_obj)
else:
    print(number)