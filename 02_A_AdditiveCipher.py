def encrypt(message, key):
    cipher = ""
    for ch in message:
        if ch.isalpha():  # only letters
            base = ord("A") if ch.isupper() else ord("a")
            cipher += chr((ord(ch) - base + key) % 26 + base)
        else:
            cipher += ch
    return cipher


def decrypt(cipher, key):
    plain = ""
    for ch in cipher:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            plain += chr((ord(ch) - base - key) % 26 + base)
        else:
            plain += ch
    return plain


#  Main
msg = input("Enter message: ")
k = int(input("Enter key (shift): "))

enc = encrypt(msg, k)
dec = decrypt(enc, k)

print("Encrypted message:", enc)
print("Decrypted message:", dec)
