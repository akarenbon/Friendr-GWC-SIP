print("Hello, I am a name generator.")
print("What type of names are you looking for?")
print("1- Masculine")
print("2- Feminine")
print("3- Unisex")
print("4- Any")

import random
type = input("Please type in the corresponding number to the category of your choice.")

masculine = ["Bob", "Stevie", "Fred", "Oliver", "Gilbert", "John", "Jeremy", "Jimmy", "Marty", "Rodrick"]
if type == "1":
    print("Here's one:")
    print(random.choice(masculine))

feminine = ["Bobina", "Tracy", "Stacy", "Becky", "Brittany", "Patricia", "Karen", "Sharon", "Susan", "Lauren"]
if type == "2":
    print("Here's one:")
    print(random.choice(feminine))

unisex = ["Sam", "Alex", "Taylor", "Morgan", "Jesse", "Micah", "Angel", "Zion", "Ren"]
if type == "3":
    print("Here's one:")
    print(random.choice(unisex))

any = ["Bob", "Stevie", "Fred", "Oliver", "Gilbert", "John", "Jeremy", "Jimmy", "Marty", "Rodrick", "Bobina", "Tracy", "Stacy", "Becky", "Brittany", "Patricia", "Karen", "Sharon", "Susan", "Lauren", "Sam", "Alex", "Taylor", "Morgan", "Jesse", "Micah", "Angel", "Zion", "Ren"]
if type == "4":
    print("Here's one:")
    print(random.choice(any))
