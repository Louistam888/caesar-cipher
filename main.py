alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text=""
  for i in plain_text: 
    position = alphabet.index(i)
    new_position = position + shift_amount
    new_letter= alphabet[new_position]
    cipher_text+=new_letter
    
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
  deciphered_text=""
  for j in cipher_text:
    position = alphabet.index(j)
    new_position = position - shift_amount
    new_letter = alphabet[new_position]
    deciphered_text+= new_letter
  
  print(f"The deciphered text is {deciphered_text}")

if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)
