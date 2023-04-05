import art

from art import logo 
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  final_text =""
  
  if cipher_direction == "decode":
    shift_amount *= -1

  for i in start_text: 
    if i in alphabet:
      position = alphabet.index(i)
      new_position = position + shift_amount
      new_letter = alphabet[new_position]
      final_text+= new_letter
    else: 
      final_text += i
  
  print(f"The {cipher_direction}d text is {final_text}")

should_continue = True

while should_continue: 
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(text, shift, direction)

  ask = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")

  if ask == "no":
    should_continue= False
    print("Goodbye!")
  




