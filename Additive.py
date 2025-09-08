def additive_decrypt(ciphertext):
    ciphertext = ciphertext.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for key in range(26):
        plaintext = ""
        for ch in ciphertext:
            if ch.isalpha():
            
                c_index = alphabet.index(ch)
                # Decrypt using formula P = (C - k) mod 26
                p_index = (c_index - key) % 26
                plaintext += alphabet[p_index]
            else:
                plaintext += ch
        print(f"Key {key:2d}: {plaintext}")


# Given ciphertext
cipher = "UDUCOYIQFFHEQSXYD"
additive_decrypt(cipher)
