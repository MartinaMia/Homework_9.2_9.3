# User enters a number between 1 and 100
# FizzBuzz program starts to count to that number (it prints them in the Terminal).
# In case the number is divisible with 3, it prints "fizz" instead of the number.
# If the number is divisible with 5, it prints "buzz".
# If it's divisible with both 3 and 5, it prints "fizzbuzz".

last_number = int(input("Select a number between 1 and 100."))

for number in range(1, last_number+1):

    if number % 3 == 0 and number % 5 == 0:         # doppelte Annamhe muss als erstes geprüft werden
        print("fizzbuzz")

    elif number % 5 == 0:
        print("buzz")

    elif number % 3 == 0:
        print("fizz")

    else:                                       # muss als sonstiges als letztes stehen 
        print(number)
