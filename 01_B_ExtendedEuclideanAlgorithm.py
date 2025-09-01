def extended_gcd(a, b):
    if b == 0:  # stop when b becomes zero
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
g, x, y = extended_gcd(a, b)

print("GCD =", g)
print("x =", x, "y =", y)
