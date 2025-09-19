p = 17
q = 23
e = 5
n = p * q   

plaintext = "HOANGTHITHUYTRANG"

print("Plaintext:", plaintext)
print("n =", n)

ciphertext = []

for ch in plaintext:
    m = ord(ch)              
    c = pow(m, e, n)       
    ciphertext.append(c)
    print(f"{ch} -> ASCII {m} -> Cipher {c}")

print("\nCiphertext sequence:")
print(" ".join(map(str, ciphertext)))
