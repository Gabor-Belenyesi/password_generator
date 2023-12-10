import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
while True:
  print("Welcome to the PyPassword Generator!")
  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))

  random_letters = []
  random_symbols = []
  random_numbers = []
  
  for letter in range(0, nr_letters):
    random_letters.append(random.choice(letters))
  for symbol in range(0, nr_symbols):
    random_symbols.append(random.choice(symbols))
  for number in range(0, nr_numbers):
    random_numbers.append(random.choice(numbers))
  
  password = random_letters + random_symbols + random_numbers
  random.shuffle(password)
  print(f"Your password is: {''.join(password)}")
  user_input = input("Would you like to make a new one? 'Y' or 'N' ")
  if user_input.upper() != "Y":
    print("Ok, bye!")
    break