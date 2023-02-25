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

def fibo(number):
    start = 1
    next = 1
    counter = 4

    while True:
        current = start + next
        if current == number:
            return counter
        if current > number:
            return -1
        start = next
        next = current
        counter += 1


a = int(input("Enter your positive number over 1:  "))
print(fibo(a))

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