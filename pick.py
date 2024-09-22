''' 
Slide 10 

'''

def check_guess(guess, answer):
    if guess == answer:
        return 0
    

def test_check_guess_correct():
    assert check_guess(5, 5) == 0 

def main():

    test_check_guess_correct()
    #print(check_guess(5, 5))

main()
