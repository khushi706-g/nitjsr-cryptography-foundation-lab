from math import gcd


#  find modular inverse of 'a' under mod 'm'
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def multiplicative_decrypt(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ciphertext.upper()

    # Possible keys (coprime with 26)
    possible_keys = [k for k in range(1, 26) if gcd(k, 26) == 1]

    for key in possible_keys:
        inv_key = mod_inverse(key, 26)
        if inv_key is None:
            continue  # Skip if inverse doesn't exist

        plaintext = ""
        for ch in ciphertext:
            if ch.isalpha():
                c_index = alphabet.index(ch)
                p_index = (c_index * inv_key) % 26
                plaintext += alphabet[p_index]
            else:
                plaintext += ch
        print(f"Key {key} (Inverse {inv_key}): {plaintext}")


# Given ciphertext
cipher = "TQKECDIVYIBIVI"
multiplicative_decrypt(cipher)
