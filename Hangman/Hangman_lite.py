import random


def Hangman():
    print("Привет! Добро пожаловать в игру Виселица")

    wordlist = ["мандарин", "яблоко", "груша", "виноград", "апельсин", "манго"]
    secret = random.choice(wordlist)
    guesses = "ауоыиэяюёе"
    turns = 5

    while turns > 0:
        missed = 0
        for letter in secret:
            if letter in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
                missed += 1

        if missed == 0:
            print("\nТы выиграл!")
            break

        guess = input("\nНазови букву: ")
        guesses += guess

        if guess not in secret:
            turns -= 1
            print("\Не угадал.")
            print("\n", "Осталось попыток: ", turns)
            if turns < 5:
                print("\n  |  ")
            if turns < 4:
                print("  0  ")
            if turns < 3:
                print(" /|\ ")
            if turns < 2:
                print("  |  ")
            if turns < 1:
                print(" / \ ")
            if turns == 0:
                print("\n\nЭто слово: ", secret)


ans = "да"
while ans == "да":
    Hangman()
    print("Хочешь сыграть снова? (да или нет)")
    ans = input()
