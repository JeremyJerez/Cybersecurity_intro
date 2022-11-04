from string import digits
from itertools import product

for combination in product(digits, repeat =8):
    print(*combination)
#prints ever 
