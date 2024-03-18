def prime_checker(number):
    is_prime = True
    for i in range(2, round(number/2)+1):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        parint("It's not a prime number.")


n = int(input("Check this number"))
prime_checker(number=n)
