# 37. Write a function which simulates the process of throwing identical balls into n identical bins until all the bins are non-empty. How many balls are we expected to throw? Investigate and write a short report based on your observation. (2 points)
import random


def maxBalls(n):
    bins = [0]*n
    
    balls = 0
    while (True):
        balls = balls + 1
        binIndex = random.randint(0, n-1)
        bins[binIndex] += 1
        if 0 in bins:
            continue
        else:
            print(bins)
            return balls


n = int(input("Number of bins : "))

print(maxBalls(n))
