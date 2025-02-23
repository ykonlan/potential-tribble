import math
def is_prime_number(number):
    if number< 2:
        isprime=False
        return isprime
    for x in range(2,int(math.sqrt(number)) + 1):
        if number % x == 0:
            isprime = False
            return isprime
    return True
try:
    number = int(input("Enter your number for check wai\n"))
    if is_prime_number(number):
        print(f"{number} is prime my lord")
    else:
        print(f"{number} is not prime, sia")
except ValueError:
    print("Enter a valid value, massa")
    
