from random import randint


random_number = randint(1, 100)
print('Угадай число от 1 до 100')

while True:
    number = int(input('Введите число: '))

    if number < random_number:
        print('Ваше число меньше того, что загадано.')

    elif number > random_number:
        print('Ваше число больше того, что загадано.') 

    else:

        break

print('Отличная интуиция! Вы угадали число :)')

