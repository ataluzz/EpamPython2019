import operator
from functools import reduce

pythagorean = [(a, b, 1000 - a - b) for a in range(1, 1001) for b in range(1, 1001)
           if a**2 + b**2 == (1000 - a - b)**2 and a < b < (1000 - a - b)]

sum_square = sum(x for x in range(1, 101))**2 - sum(x**2 for x in range(1, 101))

self_powers = sum(x**x for x in range(1, 1001))

def champernowne():
    d = ''.join(map(str,range(1,200000)))
    return (reduce(operator.mul, [int(d[10**n - 1]) for n in range(0, 7)]))
    
print("Sum square difference: ", sum_square)
print("Special Pythagorean triplet: ", pythagorean)
print("Champernowne: ", champernowne())
print("Self powers: ", self_powers)
