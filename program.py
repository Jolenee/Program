import random

def choose_word():
    words = ['python', 'hangman', 'programming', 'developer', 'computer']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        """
    ]
    return stages[tries]

def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_word = ["_"] * len(word_to_guess)
    guessed_letters = set()
    tries = 6
    print(display_hangman(tries))
    print(" ".join(guessed_word))

    while tries > 0 and "_" in guessed_word:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good job! {guess} is in the word.")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, {guess} is not in the word.")
            tries -= 1

        print(display_hangman(tries))
        print(" ".join(guessed_word))

    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word_to_guess)
    else:
        print("You ran out of tries. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
