class MagicalPrime:
    
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
def reverse_number(n):
    return int(str(n)[::-1])

def is_magical_prime(n):
    if not is_prime(n):
        return False
    reversed_n = reverse_number(n)
    return is_prime(reversed_n)

    
    def is_magical(n):
        return n == 2 ** ((n - 1) % 10)

# Example usage:
num = int(input("Enter a number: "))
if is_prime(number):
    
    print(number, "is a prime number.")
    reversed_num = reverse_number(number)
    print("Reversed number:", reversed_number)
    if is_magical_prime(number):
        print(number, "is a magical prime number.")
    else:
        print(number, "is not a magical prime number.")
else:
    print(number, "is not a prime number.")