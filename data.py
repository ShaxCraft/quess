import random


def hello_user():
    print('Привет! ;-)')
    name_user = input('Как тебя зовут?\n')
    print()
    return name_user


def start_game():
    print('Ну что же, ' + hello_user() +
          ' ,начнем игру!\n'
          'Я загадал число от 0 до 20, сможешь угадать мое число?\n'
          'У тебя есть пять попыток.\n'
          'Удачи ;-)\n')
    game()


def game():
    quessesTaken = 0
    number = random.randint(0, 20)
    for quessesTaken in range(5):
        quess = input('\n')
        quess = int(quess)
        if quess < number:
            print('Твое число слишком мало, попробуй еще.')
        if quess > number:
            print('Число слишком большое, попробуй еще.')
        if quess == number:
            break
    if quess == number:
        quessesTaken = str(quessesTaken + 1)
        print()
        print('ОТлично! Ты угадал за ' + quessesTaken + ' попытки(ок)! :-)')
    if quess != number:
        number = str(number)
        print()
        print('Увы. Я загадал число ' + number + '.')
