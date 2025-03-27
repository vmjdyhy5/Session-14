import random
import china, austria
from latam.argentina import cook as argentina_cook
from latam.brazil import cook as brazil_cook
from latam.mexico.yucatan import cook as yucatan_cook


def cook():
    print("We are making paella.")

print("a random number is:", random.randint(1, 10))

try:
    import romania
except ModuleNotFoundError:
    print("I don't know Romania")

china.cook()
china.greet()
austria.cook()
austria.greet()
cook()
argentina_cook()
brazil_cook()
yucatan_cook()

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':

    print("prime numbers")
    print(is_prime(5))
    print(is_prime(7))


    print("not prime numbers")
    print(is_prime(6))
    print(is_prime(9))
