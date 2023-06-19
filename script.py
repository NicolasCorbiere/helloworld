emptyString = ""

def play_fizzbuzz(maxValue: int) -> None:
    for i in range(1, maxValue + 1):
        result = emptyString
        OneCondition(i,3, "Fizz ")
        OneCondition(i,5, "Buzz ")
        OneCondition(i,7, "Toto ")
        OneCondition(i,11, "Tata")
        if(result == ""):
            print(i)
        else:
            print(result)


def OneCondition(i: int,multiple: int,texte: str) -> str:
    if(i % multiple == 0):
        result += texte
    return ""

if __name__ == "__main__":
    play_fizzbuzz(100)

# add comments and tests
# don't use a whilem don't print the number if there is a Fizz, a Buzz or both
# add 7, 11

# use venv, black and mypy
# import script.py
# . venv/bin/activate
# pip install black
# black script.py
# mypy --strict script.py 
