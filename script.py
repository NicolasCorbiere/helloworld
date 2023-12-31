
class Game():
    emptyString:str = ""
    result:str = emptyString

    def play_fizzbuzz(self,maxValue: int) -> None:
        for i in range(1, maxValue + 1):
            self.result = self.emptyString
            self.OneCondition(i,3, "Fizz ")
            self.OneCondition(i,5, "Buzz ")
            self.OneCondition(i,7, "Toto ")
            self.OneCondition(i,11, "Tata")
            if(self.result == ""):
                print(i)
            else:
                print(self.result)

    def OneCondition(self,i: int,multiple: int,texte: str) -> str:
        if(i % multiple == 0):
            self.result += texte
        return ""
    
emptyString:str = ""

def play_fizzbuzz(maxValue: int) -> None:
    for i in range(1, maxValue + 1):
        result = emptyString
        result += OneCondition(i,3, "Fizz ")
        result += OneCondition(i,5, "Buzz ")
        result += OneCondition(i,7, "Toto ")
        result += OneCondition(i,11, "Tata")
        if(result == ""):
            print(i)
        else:
            print(result)

def OneCondition(i: int,multiple: int,texte: str) -> str:
    if(i % multiple == 0):
        return texte
    return ""
if __name__ == "__main__":
    play_fizzbuzz(100)
    #Game().play_fizzbuzz(100)

# add comments and tests
# don't use a whilem don't print the number if there is a Fizz, a Buzz or both
# add 7, 11

# use venv, black and mypy
# import script.py
# . venv/bin/activate
# pip install black
# black script.py
# mypy --strict script.py 
