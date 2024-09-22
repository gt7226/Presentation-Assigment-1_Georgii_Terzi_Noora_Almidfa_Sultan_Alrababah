''' Slide 11 and 12''' 

def check_guess(guess, answer):

    difference = guess - answer
    
    if guess == answer:
        print("You guessed the number!")
        return 0
    
    elif guess > answer:
        print(f"Your guess was {difference} away from the number.")
        return difference
    
    else:
        guess < answer
        print(f"Your guess was {difference} away from the number.")
        return difference



def test_check_guess_correct():
    assert check_guess(1, 1) == 0

def test_check_guess_too_high():
    assert check_guess(7, 5) == 2

def test_check_guess_too_low():
    assert check_guess(5, 3) == 2

def main():
    test_check_guess_correct()  
    test_check_guess_too_high()
    test_check_guess_too_low()
    

main()
