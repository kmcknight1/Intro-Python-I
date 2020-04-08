import time
from colorama import init, Fore
init(autoreset=True)


'''Stretch goal explanation: 

   Write a program to determine if a number, given on the command line, is prime.

   1. How can you optimize this program?
   2. Implement [The Sieve of
      Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
      of the oldest algorithms known (ca. 200 BC).'''


red = Fore.RED
green = Fore.GREEN

yes = green + "Yes, this number is prime :D"
no = red + "No, this number is not prime :("


def prime_checker(x):
    if x > 1:
        for i in range(2, x//2):
            if (x % i) == 0:
                print("1", x, no)
                break
        else:
            print("2", x, yes)
    else:
        print("3", x, no)


loop = True
while(loop):
    num_input = input(
        'Enter a number to discover whether it is PRIME ("ooo ahhh"):')
    try:
        num_input = int(num_input)
        prime_checker(num_input)
    except:
        print("You must enter a number!")
        time.sleep(0.5)
