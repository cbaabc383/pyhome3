# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[0..N-1]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

count = 0
N = int(input("Enter the number of elements in the array:"))
X = int(input("Enter the element you are interested in:"))
A = [0] * N
for i in range(N):
    A[i] = int(input("Enter the element:"))
    # print (array[i])
    if X == A[i]:
        count += 1
print (f"Element {X} occurs {count} times.")

