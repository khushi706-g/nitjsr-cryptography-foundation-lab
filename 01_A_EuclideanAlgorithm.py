def euclidean_gcd(a, b):
    while b != 0:  
        r = a % b  
        a = b  
        b = r  
    return a 



x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("GCD is:", euclidean_gcd(x, y))
