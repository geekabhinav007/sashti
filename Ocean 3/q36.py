# 36. Write a function which simulates the process of throwing n identical balls into n bins. What is the maximum across the buckets? Write a short report on the output of your code. (2 points)

import random


def throwBall(n):
    bins = [0] * n
    for i in range(n):
        bin_index = random.randint(0, n-1)
        bins[bin_index] += 1
    maxi = max(bins)
    return maxi


n = int(input("Enter Number of bins : "))

print(throwBall(n))
