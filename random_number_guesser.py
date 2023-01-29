import random

# Write your code here.
# Make sure to use `random.randint` to pick your random number.
while True:
    try:
        num1 = int(input("Enter the start of the range: "))
        break
    except:
        print("Please enter a valid number.")
while True:
    num2 = int(input("Enter the end of the range: "))
    if num2>num1:
        break
    else:
        print("Please enter a valid number.")

random_num = random.randint(num1, num2)
cont = 0
while True:
    try:
        guess = int(input("Guess a number: "))
        cont += 1
        if guess == random_num:
            if cont>1:
                print(f"You guessed the number in {cont} attempts")
                break
            if cont==1:
                print(f"You guessed the number in {cont} attempt")
                break
    except:
        print("Please enter a valid number.")
        

        