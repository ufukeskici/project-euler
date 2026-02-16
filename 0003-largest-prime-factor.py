'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143
'''

i = 2
prime_factors = []
number = 600851475143

while i < number:
    if number % i == 0:
        if len(prime_factors) > 0:
            if number == prime_factors[-1]:
                prime_factors.pop()
        prime_factors.append(i)
        result = number // i
        prime_factors.append(result)
        number = result
    else:
        i = i + 1

print(max(prime_factors))