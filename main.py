import random

words = ["developer", "python", "javascript", "compiler", "programming", "java", "database", "rust", "html", "backend", "loops", "recursion", "css", "github", "react", "function"]

word_selected = random.choice(words)
display_words = ["_" for _ in word_selected] # this will create underscores in place of the letters
attempts = 10

print("Hangman Game!")

while attempts > 0 and "_" in display_words:
    print(f"\nAttempts left: {attempts} attempts")
    print("\n" + " ".join(display_words))
    guess = input("\nGuess a letter: ").lower()

    if guess in word_selected:
        for i, letter in enumerate(word_selected):
            if letter == guess:
                display_words[i] = letter
    else:
        print("That letter is not in the word! Try again.")
        attempts -= 1

if "_" not in display_words:
    print(f"\nYou guessed the word {"".join(display_words)} correctly!")
else:
    print(f"\nSorry, you ran out of attempts. The correct word was {word_selected}.")