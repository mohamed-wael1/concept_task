import random

def word_scramble_game():
    words = ["apple", "banana", "cherry", "grape", "orange", "kiwi", "mango", "peach"]

    chosen_word = random.choice(words)
    scrambled_word = ''.join(random.sample(chosen_word, len(chosen_word)))
    attempts = 5 
    print("Welcome to the word scramble game!")
    print(f"Try to guess the original word from the scrambled word: {scrambled_word}")
    print(f"You have {attempts} attempts.")

    while attempts > 0:
        guess = input("Enter your guess: ").strip()

        if not guess:
            print("Please enter a valid guess.")
            continue
        if guess == chosen_word:
            print("Congratulations! You guessed the correct word.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect! Try again. You have {attempts} attempts left.")
            else:
                print(f"You are out of attempts. The correct word was: {chosen_word}")

word_scramble_game()
