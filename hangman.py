import random

status = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

logo  = """
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝"""

print(f"{logo}\n\n    Welcome to the Hangman Game. ")

lives = 6


secret_word = ["cipher","hacker","professor","lucifer","linux","kernal"]

choosen_word = random.choice(secret_word)
word_length = len(choosen_word)

display = []
for _ in range(word_length):
    display += "_"

print()
print(display)
print()

end_of_game = False

while not end_of_game:
    user_guess = input("Gues your letter: ").lower()
    for position in range(word_length):
        letter = choosen_word[position]
        if letter == user_guess:
            display[position] = letter
    
        
    if user_guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print("===========================")
    print()
    print(display)

    
    print(status[lives]) 

    if "_" not in display:
        end_of_game = True
        print("You won!") 