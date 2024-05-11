import random

hidden_number = random.randint(1, 10)

print("Welcome to the Guessing Game with Multiple Chances!")
print("You have 3 chances to guess the hidden number.")

for chance in range(3):
    guess = int(input("Guess the number 1 to 10: "))
    
    if guess == hidden_number:
        print("Congratulations! You guessed the correct number! You may now rest!")
        break
    else:
        
        if guess < hidden_number:
            print("Higher pa!")
        else:
            print("Lower pa!")
else:
    print("Sorry, you ran out of chances. The hidden number was", hidden_number)
    print("Try Again?")
