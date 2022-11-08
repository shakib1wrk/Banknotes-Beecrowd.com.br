notes = int(input())

print(notes)

n, y = divmod(notes, 100)
print(n, "nota(s) de R$ 100,00")

n, y = divmod(y, 50)
print(n, "nota(s) de R$ 50,00")

n, y = divmod(y, 20)
print(n, "nota(s) de R$ 20,00")

n, y = divmod(y, 10)
print(n, "nota(s) de R$ 10,00")

n, y = divmod(y, 5)
print(n, "nota(s) de R$ 5,00")

n, y = divmod(y, 2)
print(n, "nota(s) de R$ 2,00")

n, y = divmod(y, 1)
print(n, "nota(s) de R$ 1,00")