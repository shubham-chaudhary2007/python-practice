#Prime Number Analyzer:
#Take a positive integer as input.
#Determine whether it is prime, and print all its factors using loops.



pn = int(input("enter positive number: "))

if pn < 1:
    print("its not a prime number")
else:
    factors = []
    count = 0

    for i in range(1, pn + 1):
        if pn % i == 0:
            factors.append(i)
            count += 1

    print(f"factors of {pn}: {factors}")

    if count == 2:
        print("its a prime number")
    else:
        print("its not a prime number")