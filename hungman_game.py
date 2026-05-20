import random
words = ["python", "apple", "tiger", "school", "laptop"]
word = random.choice(words)
hidden_word = ["_"] * len(word)
guessed_letters = []
wrong_guesses = 0
stages = [
'''
-----
|   |
    |
    |
    |
    |
=========
''',

'''
-----
|   |
O   |
    |
    |
    |
=========
''',

'''
-----
|   |
O   |
|   |
    |
    |
=========
''',

'''
-----
|   |
O   |
/|  |
    |
    |
=========
''',

'''
-----
|   |
O   |
/|\ |
    |
    |
=========
''',

'''
-----
|   |
O   |
/|\ |
/   |
    |
=========
''',

'''
-----
|   |
O   |
/|\ |
/ \ |
    |
=========
'''
]

print("===== HANGMAN GAME =====")

while wrong_guesses < 6 and "_" in hidden_word:

    print("\nWord:", " ".join(hidden_word))

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:

        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess

    else:
        wrong_guesses += 1

        print(stages[wrong_guesses])

        print("Wrong Guess!")
        print("Attempts Left:", 6 - wrong_guesses)

if "_" not in hidden_word:

    print("\nYou Win!")
    print("The word was:", word)

else:

    print("\nGame Over!")
    print(stages[6])
    print("The correct word was:", word)