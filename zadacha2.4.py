## Петя впервые пришел на урок физкультуры в новой школе. Перед началом урока ученики выстраиваются по росту, в порядке невозрастания. Напишите программу, которая определит на какое место в шеренге Пете нужно встать, чтобы не нарушить традицию, если заранее известен рост каждого ученика и эти данные уже расположены по невозрастанию (то есть каждое следующее число не больше предыдущего). Если в классе есть несколько учеников с таким же ростом, как у Пети, то программа должна расположить его после них.

n = int(input("кол-во учеников "))
spisok = list()
for i in range(n):
    k = int(input())
    spisok.append(k)
print(spisok)
spisok2 = sorted(spisok, reverse=True)
print(spisok2)
r = int(input("Введите рост нового ученика "))
j=1
for i in spisok2:
    if r <=i:
        j+=1
print(f"место нового ученика в шеренге  {j}")