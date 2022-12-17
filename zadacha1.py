# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
from random import randint
n = int(input("Введите кол-во монет "))
coins = list()
gerb = 0
resh = 0
for i in range(n):
    coins.append(randint(0,1))
print(coins)

for i in coins:
    if i == 0:
        gerb += 1
    else:
        resh += 1

print(min(gerb, resh))

