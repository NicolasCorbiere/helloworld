def play_fizzbuzz(maxValue: int) -> None:
    for i in range(1, maxValue + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    play_fizzbuzz(25)

# add comments and tests
# don't use a whilem don't print the number if there is a Fizz, a Buzz or both
# add 7, 11

# use venv, black and mypy
# import script.py
# . venv/bin/activate
# pip install black
# black script.py
# mypy --strict script.py 
