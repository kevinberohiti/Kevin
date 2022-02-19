



import random
guess=""
a = random.randint(0, 100)
print(a)

while guess != a :
    guess = int(input("Enter a number: "))
    if guess > a:
        print("Too high!")
    elif guess < a:
        print("Too low!")
    else:
        print("Just right!")


















