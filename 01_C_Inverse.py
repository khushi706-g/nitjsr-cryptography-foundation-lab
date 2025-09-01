def extended_gcd(a, b):
    # when b = 0, gcd is a
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def mod_inverse(a, p):
    gcd, x, y = extended_gcd(a, p)
    if gcd != 1:
        return None  # no inverse if gcd ≠ 1
    else:
        return x % p  # make sure result is positive


# ---- Main ----
a = int(input("Enter a number: "))
p = int(input("Enter prime modulus p: "))

inverse = mod_inverse(a, p)

if inverse is None:
    print("No inverse exists!")
else:
    print(f"Inverse of {a} mod {p} = {inverse}")
    
