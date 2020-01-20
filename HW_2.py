#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# for i in range(1, 6):
#     print(i, 0)



'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# n = 0
# for i in range(10):
#     a = int(input('Введите цифру '))
#     if a == 5: n += 1
# print('Колличество цифр "5"  = ', n)



'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum += i
# print(sum)



'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# pr = 1
# for i in range(1,11):
#     pr *= i
# print(pr)


'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
# n = input('Введите число: ')
# for i in n:
#   print(i)

'''
Задача 6
Найти сумму цифр числа.
'''
# n = int(input('Введите число: '))
# sum = 0
#
# while n > 0:
#     sum += n % 10
#     n= n //10
# print(sum)

'''



Задача 7
Найти произведение цифр числа.
'''
# n = int(input('Введите число: '))
# pr = 1
#
# while n > 0:
#     pr *= n % 10
#     n= n //10
# print(pr)



'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 2134135
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# integer_number = int(input('Введите число '))
# m = 0
# while integer_number > 0:
#     if integer_number%10 > m:
#         m = integer_number %10
#     integer_number = integer_number //10
# print(m)

'''
Задача 10
Найти количество цифр 5 в числе
'''
# integer_number = int(input('Введите число '))
# n=0
# while integer_number > 0:
#     if integer_number%10 == 5:
#         n += 1
#     integer_number = integer_number//10
# print('Колличество цифр "5" в числе = ', n)