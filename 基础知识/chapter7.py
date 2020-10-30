#%%

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# %%
message = input("input your name: ")
print("hello "+message.title()+" !")


# %%
prompt="first line."
prompt += "\nsecond line."
prompt += "\nthird line."
name = input(prompt)
print(name)


# %%
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


# %%
sandwish_orders=['A_sandwish','B_sandwish','C_sandwish']
finished_orders=[]
while sandwish_orders:
    current_sanwish = sandwish_orders.pop()
    print("I made your "+current_sanwish)
    finished_orders.append(current_sanwish)
print(finished_orders)

# %%
sandwish_orders=['pastrami','A_sandwish','B_sandwish','pastrami','pastrami']
print("pastrami sold out!")
while 'pastrami' in sandwish_orders:
    sandwish_orders.remove('pastrami')
print(sandwish_orders)


# %%
