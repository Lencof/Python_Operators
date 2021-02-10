# __Author__ __Lencof__
# if.py

number = 70
guess = int(imput('Введите целое число :'))

if guess == number:
    print('Поздравляю, вы угадали.')
    print('Хотя и не выграли никакого приза!')
elif guess < number:
    print('Нет загаданное число немного больше этого.')
    
else:
    print('Нет, загаданное число немного больше этого .')
  
print('Завершено')
