import random
def guess():
    print("Hello! What is your name?")
    name = input()
    print(f"Well,{name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1,20)
    guess_taken = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guess_taken +=1
        if guess_taken < number:
            print("Your guess is too low.")
        elif guess_taken > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guess_taken} guesses!")
guess()