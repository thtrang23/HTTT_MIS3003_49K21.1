plaintext = "HOANG THI THUY TRANG"
k = 48
ciphertext = ""

for char in plaintext:
    if char == " ": 
        ciphertext += " "
    else:
        
        x = ord(char) - ord('A')
      
        x = (x + k) % 26
       
        ciphertext += chr(x + ord('A'))

print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)
