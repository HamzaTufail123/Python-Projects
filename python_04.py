import random

def Guessing_Game():
    words = ["python", "data", "science", "ai", "model", "neuron"]
    guess = []

    difficulty = input("Choose difficulty(easy\medium\hard): ").lower()
    if difficulty == "easy":
        attempts = 7
    elif difficulty == "medium":
        attempts = 5
    else:
        attempts = 3

   
    secrets_word = random.choice(words)
    print("-" * 40)
    print("🎮 Welcome to the Word Guessing Game! ")
    print("Guess the secret word you have 5 attepts. ")

    while attempts > 0:
        user_word = input(f"\nEnter word from {words} list: \n").lower()
        guess.append(user_word)
        if user_word == secrets_word:
            print(
                f"✅ Correct you enterd `{user_word}` in {6 - attempts} attempts.Cheer's. "
            )
            break
        else:
            attempts -= 1
            print(f"❌ Wrong guess. Attempts left: {attempts}")

            if attempts > 0:
                print(f"Hint: Word start with {secrets_word[0]} and has {len(secrets_word)} letter's. ")

    if attempts == 0:
        print("Game over. ")

    score = 0
    score += attempts
    print("-" * 40)
    print(f"Final Score: {score}")
    print(f"List of user guess: {guess}")

Guessing_Game()



