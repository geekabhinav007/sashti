def gcd(a,  b):
    if (a == 0):
        return b
    return gcd(b % a, a)


a, b = input().split()

print("GCD of", a, "and", b, "is", gcd(int(a), int(b)))
