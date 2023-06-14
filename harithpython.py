import random
actual_num = random.randint(1, 100)
guess = int(input("Enter a number 1 to 100 : "))
while True:
    if guess < actual_num:
        print ("guess is low")
        guess = int(input("Enter a number from 1 to 100 : "))
    elif guess > actual_num:
        print ("guess is high")
        guess = int(input("Enter a number  from 1 to 100 : "))
    else:
        print ("Congradulations your guessed number is correct !!!! ")
        break