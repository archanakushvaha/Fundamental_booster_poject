print("Welcome to the Interactive Personal Data Collector")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height: "))
favourite_num = int(input("Please enter your favourite_num: "))

print("Thank you! Here is the information we collected:")

print(f"Name: {name}: Type: {type (name)}: ,Memory Address: {id (name)}")
print(f"age: {age}: Type: {type (age)}: ,Memory Address: {id (age)}")
print(f"height: {height}: Type: {type (height)}: ,Memory Address: {id (height)}")
print(f"favourite_num: {favourite_num}: Type: {type (favourite_num)}: ,Memory Address: {id (favourite_num)}")

current_year=2026

birth_year=current_year-age

print(f"Your birth year is approximately: {birth_year} (based on your age of 18)")

print("Thank you for using the personal Data collector. Goodbye!")
