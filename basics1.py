name= input("Enter  your name:")

birth_year = int(input("Enter your birth year:"))

current_year = 2026

age = current_year - birth_year

if birth_year > current_year:
    print("Error: Birth year cannot be in the future")

elif age > 120:
    print("Error: please enter a realistic birth year")

else:
    print(f"\nHello,{name} !")
    print(f"You are {age} years old.")