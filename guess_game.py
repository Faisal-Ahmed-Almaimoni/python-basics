import random
number = random.randint(1,10)
attempts = 0
while True:
    guess = int(input(" guess the number (1-10)"))
    attempts = attempts + 1
    if guess == number:
        print("correct! you took " + str(attempts) + " attempts")
        break
    elif guess < number:
        print("too low! try higher")
    else:
        print("too high! try lower")
        