def play_fizzbuzz(maxValue:int)->None:
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
    play_fizzbuzz(2.5)

# add comments and tests
# don't use a whilem don't print the number if there is a Fizz, a Buzz or both
