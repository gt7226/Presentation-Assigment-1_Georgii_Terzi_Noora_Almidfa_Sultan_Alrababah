from random import randrange

def check_guess(guess, answer):
    difference = guess - answer  

    if guess == answer:
        print("You guessed the number!")
        return 0
    elif guess > answer:
        print(f"Your guess was {difference} away from the number.")
        return difference
    else:
        difference = answer - guess  
        print(f"Your guess was {difference} away from the number.")
        return difference

def main():
    answer = randrange(1, 10)  
    guess = int(input("Pick a number between 1 and 10: "))
    result = check_guess(guess, answer)
    return result

if __name__ == "__main__":
    main()
