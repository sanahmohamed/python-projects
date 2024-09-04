# import random

# def guessing_game():
#     rand_num=random.randint(1,10)
    
#     attempts=0

#     while attempts<3:
#         guess=int(input("enter the number to guess: "))
#         attempts+=1

#         if guess==rand_num:
#             print("you guessed right number!!!!")
#             print(f"ysss the number is {rand_num}")
#             break
#         else:
#             print("you guessed wrong number!!!oopsss")
#     else:        
#         print(f"The number is {rand_num}")

# print(guessing_game())




import random

def guessing_game():
    number_to_guess = random.randint(1, 10)
    
    attempts = 0
    max_attempts = 3
    
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    print(f"You have {max_attempts} attempts to guess the correct number.")
    
    while attempts < max_attempts:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
    else:
        print("Please enter a valid number.")
        
        if attempts == max_attempts:
            print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}.")


print(guessing_game())
