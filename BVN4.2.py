def encrypt(plaintext, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    k = k % 26   
    ciphertext = ""

    for ch in plaintext:
        if ch.isalpha():  
            idx = alphabet.index(ch.lower())   
            c_idx = (idx + k) % 26             
            ciphertext += alphabet[c_idx].upper()  
        else:
            ciphertext += " " 
    return ciphertext


plaintext = "hoang thi thuy trang"
k = 48
ciphertext = encrypt(plaintext, k)

print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)
