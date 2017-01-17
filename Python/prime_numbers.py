# Small program to list numbers from 2 and print if they are prime or not

max_number = 100

for n in range(2, max_number):
    for x in range (2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
