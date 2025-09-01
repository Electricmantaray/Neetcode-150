"""
Algorithm: Random List generator


Description:
    Generates a list of random integers
    seperated with a space for my sorting
    algorithm benchmarks

        
"""

# Imports
from random import randint

# Variable inputs
n = int(input("Length of List: "))
min, max = int(input("Minimum value in range: ")), int(input("Maximum value in range: "))

# Main Implimentation

class listGen:
    def generate(self, n, min, max):
        result = []

        for i in range(n):
            result.append(str(randint(min, max)))
        
        return ' '.join(result)

print(listGen().generate(n, min, max))
