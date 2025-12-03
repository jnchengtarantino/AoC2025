import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    result = []
    for bank in parseInput(lines):
        currMax = 0
        for i in range(len(bank)):
            for j in range(i+1, len(bank)):
                currMax = max(currMax, (bank[i]*10) + bank[j])
        result.append(currMax)

    return sum(result)
    

def part2(lines):
    result = []
    for bank in parseInput(lines):
        agg = 0
        currMaxJ = 0

        for i in range(12):
            for j in range(currMaxJ, len(bank) - (11-i)):
                if bank[j] > bank[currMaxJ]: currMaxJ = j
            agg += bank[currMaxJ] * (10 ** (11-i))
            currMaxJ += 1

        result.append(agg)
    
    return sum(result)

    
def parseInput(lines: list[str]):
    return [[int(x) for x in bank.strip()] for bank in lines]

if __name__ == "__main__":
    # testFile = open("test.txt")
    # testLines = testFile.readlines() 
    # print(" --- TEST --- ")
    # print(f'Part 1 : {part1(testLines)}')      
    # print(f'Part 2 : {part2(testLines)}')
    # testFile.close()

    inFile = open("in.txt") 
    inLines = inFile.readlines()
    print(" --- RESULT --- ")
    print(f'Part 1 : {part1(inLines)}')      
    print(f'Part 2 : {part2(inLines)}')
    inFile.close()