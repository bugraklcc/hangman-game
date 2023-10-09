import random
import json

# Read words from the JSON file
with open("words.json", "r") as file:
    word_data = json.load(file)
    words = word_data.get("words", [])


# Hangman game code
def main():
    word = random.choice(words)
    hangman = ['''
      +---+
      o   |
     /|\  |
     / \  |
         ---''', '''
      +---+
      o   |
     /|\  |
     /    |
         ---''', '''
      +---+
      o   |
     /|\  |
          |
         ---''', '''
      +---+
      o   |
     /|   |
          |
         ---''', '''
      +---+
      o   |
     /    |
          |
         ---''', '''
      +---+
      o   |
          |
          |
         ---''', '''
      +---+
          |
          |
          |
         ---''']

    correct_letters = []
    wrong_letters = []
    attempts = len(hangman)

    def hint(word):
        length = len(word)
        if length < 5:
            return "The word is very short."
        elif length < 8:
            return "The word is of medium length."
        else:
            return "The word is long."

    print("Welcome! Let's play Hangman.")
    print("Hint:", hint(word))

    while attempts > 0:
        out = ""
        for letter in word:
            if letter in correct_letters:
                out += letter
            else:
                out += "_"

        if out == word:
            break

        print("Word: ", out)
        print(hangman[attempts - 1])
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        if guess in correct_letters or guess in wrong_letters:
            print(guess, "Already guessed.")
        elif guess in word:
            print("Correct letter")
            correct_letters.append(guess)
        else:
            print("Wrong letter..!")
            attempts -= 1
            wrong_letters.append(guess)

    if attempts != 0:
        print("Congratulations! You won. The word was: ", word)
    else:
        print("Sorry, you lost. The word was: ", word)


if __name__ == "__main__":
    main()
