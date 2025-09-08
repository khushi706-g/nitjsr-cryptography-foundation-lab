from math import gcd


#  find modular inverse
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_decrypt(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ciphertext.upper()

    # Possible 'a' values (coprime with 26)
    possible_a = [k for k in range(1, 26) if gcd(k, 26) == 1]

    for a in possible_a:
        a_inv = mod_inverse(a, 26)
        if a_inv is None:
            continue
        for b in range(26):  # b can be 0–25
            plaintext = ""
            for ch in ciphertext:
                if ch.isalpha():
                    c_index = alphabet.index(ch)
                    p_index = (a_inv * (c_index - b)) % 26
                    plaintext += alphabet[p_index]
                else:
                    plaintext += ch
            print(f"a={a}, b={b} -> {plaintext}")


# Given ciphertext
cipher = "RXQMHSJDGGDRVGHJF"
affine_decrypt(cipher)
