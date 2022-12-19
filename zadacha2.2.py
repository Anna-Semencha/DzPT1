#Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

n = int(input("Введите число "))
numbers = list(range(1, n+1))
print(numbers)
print(sum(numbers))