# This is a sample Python script.
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':

   letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
   symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

   print("Welcome to the PyPassword Generator!")

   nr_letters = int(input("How many letters would you like in your password?\n"))
   nr_symbols = int(input(f"How many symbols would you like?\n"))
   nr_numbers = int(input(f"How many numbers would you like?\n"))

   PasswordList = []

   for i in range(0, nr_letters):
      randLetter = random.randint(0, len(letters) - 1)
      PasswordList.append(letters[randLetter])

   for i in range(0, nr_numbers):
      randNum = random.randint(0, len(numbers) - 1)
      PasswordList.append(numbers[randNum])

   for i in range(0, nr_symbols):
      randSym = random.randint(0, len(symbols) - 1)
      PasswordList.append(symbols[randSym])

   for i in range(0, len(PasswordList)):
      randPlacement1 = random.randint(0, len(PasswordList) - 1)
      randPlacement2 = random.randint(0, len(PasswordList) - 1)
      Swap = PasswordList[randPlacement1]
      PasswordList[randPlacement1] = PasswordList[randPlacement2]
      PasswordList[randPlacement2] = Swap

   Password = ""

   for i in PasswordList:
      Password += i

   print(Password)



