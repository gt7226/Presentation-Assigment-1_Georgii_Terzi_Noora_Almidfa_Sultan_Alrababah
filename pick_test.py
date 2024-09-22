import pick1

def test_check_guess_correct():
    assert pick1.check_guess(5, 5) == 0

def test_check_guess_too_high():
    assert pick1.check_guess(7, 5) == 2

def test_check_guess_too_low():
    assert pick1.check_guess(3, 5) == 2

if __name__ == "__main__":
    import pytest
    pytest.main()
