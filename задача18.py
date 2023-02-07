# Задача 18: Требуется найти в массиве A[0..N-1] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих строках записаны N целых чисел A[i]. 
# Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6

# -> 5

mini = 0
N = int(input("Enter the number of elements in the array:"))

A = [0] * N
for i in range(N):
    A[i] = int(input("Enter the element: "))
print (A)
X = int(input("Enter the number you are interested in: "))
mini = 10000
for i in range(N):
    ABC = X - A[i]
    if ABC < 0:
        ABC = -ABC
        
    if ABC < mini:
        mini = ABC
        num = A[i]
print(f"Nearest number is {num}")
