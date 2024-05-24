from random import shuffle
from sys import exit


GAME_NAME = "Виселица"
ANON_NAME = "Анонимус"
ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
FILENAME = "test.txt"
MIN_LENGTH = 5
BS = "\\"

wants_to_play = True
hit = 0
miss = 0

x = (39 - len(GAME_NAME)) // 2
y = 1 if len(GAME_NAME) % 2 == 0 else 0

print("* " * 20 + "*")
print("*" + " " * 39 + "*")
print("*" + " " * x + GAME_NAME.upper() + " " * (x + y) + "*")
print("*" + " " * 39 + "*")
print("* " * 20 + "*")
print()

print(f'Добро пожаловать в "{GAME_NAME}"!\n')

name = input("Как тебя зовут? ")
if not name:
    name = ANON_NAME

print(f"\n{name}, правила этой игры просты.")
print("Я загадаю слово и скажу склько в нем букв. Ты будешь по ")
print("очереди называть по одной букве. Если буква есть в моем слове, я ")
print("тебе ее покажу. Ты можешь ошибиться буквой не более семи раз.")
print("")

words = []
file = open(FILENAME, encoding="utf-8")
for line in file:
    line = line.lower().strip()
    if len(line) >= MIN_LENGTH:
        russian_word = True
        for letter in line:
            if letter not in ALPHABET:
                russian_word = False
        if russian_word:
            words.append(line)
file.close()

if len(words) == 0:
    print("В файле  нет ни одного слова!")
    input("Нажми ENTER для завершения программы.")
    exit()


shuffle(words)

while wants_to_play:

    if len(words) == 0:
        print("К сожалению, у меня закончились слова!")
        wants_to_play = False
    else:
        word = words.pop()
        current_word = "-" * len(word)
        print(f"{name}, я загадал слово, состоящее из {len(word)} букв.\n")
        mistakes = 0
        letters = ""

        while not (word == current_word or mistakes > 6):

            print()
            print(f"------")
            print(f"|/  {'|' if mistakes > 0 else ' '}")
            print(f"|   {'O' if mistakes > 1 else ' '}")
            print(
                f"|  {'/' if mistakes > 2 else ' '}{'|'if mistakes > 3 else ' '}{BS if mistakes > 4 else ' '}"
            )
            print(
                f"|  {'/' if mistakes > 5 else ' '} {BS if mistakes > 6 else ' '}"
            )
            print(f"|\\")
            print(f"|_\_")
            print()

            print(f"Слово: {current_word}")
            print(f"Промахи: {mistakes} из 7")
            print(f"Названные буквы: ", end="")

            if len(letters) == 0:
                print("-")
            else:
                print(*letters)

            letter = input("Введи букву: ").lower()
            while not (len(letter) == 1 and letter in ALPHABET):
                letter = input("Введи одну букву русского алфавита: ").lower()

            letter_in_word = False
            for i in range(len(word)):
                if letter == word[i]:

                    current_word = (
                        current_word[0:i] + letter + current_word[i + 1 :]
                    )
                    letter_in_word = True
            if not letter_in_word:
                mistakes += 1
            if not letter in letters:
                letters += letter

        print()
        print(f"------")
        print(f"|/  {'|' if mistakes > 0 else ' '}")
        print(f"|   {'O' if mistakes > 1 else ' '}")
        print(
            f"|  {'/' if mistakes > 2 else ' '}{'|'if mistakes > 3 else ' '}{BS if mistakes > 4 else ' '}"
        )
        print(
            f"|  {'/' if mistakes > 5 else ' '} {BS if mistakes > 6 else ' '}"
        )
        print(f"|\\")
        print(f"|_\_")

        print()
        print(f"Слово: {current_word}")
        print(f"Промахи: {mistakes} из 7")
        print(f"Названные буквы: ", end="")

        if len(letters) == 0:
            print("-")
        else:
            print(*letters)

        print()
        if word == current_word:
            print(f"{name}, поздравляю! Ты угадал слово!")
            hit += 1
        else:
            print(f"{name}, к сожалению ты не смог угадать слово...")
            miss += 1
        print(f'Правильное слово: "{word}".')

        print()
        again = input("Хочешь сыграть еще раз (да/нет)?").lower()
        while not (again == "да" or again == "нет"):
            again = input('Просто ответь "да" или "нет":').lower()
        if again == "нет":
            wants_to_play = False

print()
print(f"{name}, спасибо за игру! Ниже результаты твоей игры:")
print(f"Угаданных слов: {hit}, количество неугаданных слов: {miss}.")
print("До новых встреч!")
input("Нажми ENTER для завершения программы.")
