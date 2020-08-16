def fizz_buzz(number):
    while True:
        if "help" in number:
                print("""
                You can check if your number is divisible by 3  and 5 (returns FizzBuzz), only 3 (returns Buzz),
                only 5 (returns Fizz) or by none (returns your starting number). 
                """)
                break

        if "quit" in number:
            quit("User quit")

        numberFormat = int(number)

        if numberFormat % 5 == 0 and numberFormat % 3 == 0:
            print("FizzBuzz")
            break

        elif numberFormat % 5 == 0:
            print("Fizz")
            break

        elif numberFormat % 3 == 0:
            print("Buzz")
            break

        else:
            print(numberFormat)
            break


while True:
    fizz_buzz(input("Enter a number: "))
