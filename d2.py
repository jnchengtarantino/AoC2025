import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    ranges = parseInput(lines)
    results = set()
    for r in ranges:
        lower, upper = r.split('-')

        for i in range(int(lower), int(upper) + 1):
            s = str(i)
            if re.match(r'^(\d+)\1$', s): results.add(int(s))
    
    return(sum(list(results)))


def part2(lines):
    ranges = parseInput(lines)
    results = set()
    for r in ranges:
        lower, upper = r.split('-')

        for i in range(int(lower), int(upper) + 1):
            s = str(i)
            if re.match(r'^(\d+)\1+$', s): results.add(int(s))
    
    return(sum(list(results)))
    
def parseInput(lines: list[str]):
    return [r for r in lines[0].split(',')]

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