# По данному целому неотрицательному n 
# вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input: 5
# Output: 120

# n = int(input("Enter your positive number over 0:  "))
# count = 1
# factorial = 1
# while count <= n:
#     factorial *= count
#     count += 1
# print(factorial)


# Дано натуральное число A > 1. 
# Определите, каким по счету числом 
# Фибоначчи оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6




# def fibo(number):
#     start = 1
#     next = 1
#     counter = 4

#     while True:
#         current = start + next
#         if current == number:
#             return counter
#         if current > number:
#             return -1
#         start = next
#         next = current
#         counter += 1


# a = int(input("Enter your positive number over 1:  "))
# print(fibo(a))




# My decision
#  a = int(input("Enter your positive number over 1:  "))
# count = 1
# fiabA = 0
# fiabB = 1
# while fiabB <= a:
#     fiabC = fiabA + fiabB
#     fiabA = fiabB
#     fiabB = fiabC
#     count += 1
#     if fiabB != a:
#         print(-1)
# print(count)


# Дано целое число N (> 1). Найти наименьшее целое число K,
#  при котором выполняется неравенство 3^K > N,
#  где 3^K - это 3 в степени K или число 3,
#  умноженное само на себя K раз.
#  Например, 3^5 = 3*3*3*3*3. Ответом в задаче
#  будет первая степень числа 3, которая больше, 
# чем заданное число N. Например, если N=41, 
# распишем степени числа три: 3^1 = 3; 3^2 = 3*3 = 9;
#  3^3 = 3*3*3 = 27; 3^4 = 3*3*3*3 = 27 * 3 = 81;. 
# Таким образом, первая степень, в которую возвести число 3,
#  превышающая число N - это 4.

# n = int(input("Enter the N: "))
# count = 0
# number = 3
# result = 0
# while result < n:
#     count += 1
#     result = number ** count

# print(count)




# 6*.Даны положительные числа A, B, C. 
# На прямоугольнике размера A x B размещено 
# максимально возможное количество квадратов 
# со стороной C (без наложений). Найти количество 
# квадратов, размещенных на прямоугольнике. 
# Операции умножения и деления не использовать.

# a = int(input("Enter the A size: "))
# b = int(input("Enter the B size: "))
# c = int(input("Enter the C size: "))
# sumA = 0
# countA = 0
# while sumA < a:
#     countA += 1
#     sumA += c
# sumB = 0
# countB = 0
# while sumB < b:
#     countB += 1
#     sumB += c
# print(countA + countB + countA + countB)





# Yставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю 
# наблюдений за погодой. Они обратились к синоптикам, а те, 
# в свою очередь, занялись исследованиями статистики за прошлые 
# годы. Их интересует, сколько дней длилась самая длинная оттепель. 
# Оттепелью они называют период, в который среднесуточная температура 
# ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую 
# синоптикам в работе. Пользователь вводит число N – общее количество 
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается 
# N целых чисел. Каждое число – среднесуточная температура 
# в соответствующий день. Температуры – целые числа и лежат 
# в диапазоне от –50 до 50
# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2


# n = int(input("Enter the amount of days: "))

# array = []
# for i in range(n):
#     array.append(int(input(f"Enter the temperature of the day {i+1}: ")))

# counter = 0
# counterMax = 0
# for i in array:
#     if i > 0:
#         counter +=1
#         if counterMax < counter:
#             counterMax = counter
#     if i < 0:
#         counter = 0

# print(counterMax)