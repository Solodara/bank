# Депозит

n = int(input('введіть розмір вкладу: '))
years = int(input('введіть кількість років на яку ви робите вклад: '))

def bank(x, y):
    while y > 0:
        x =x*0.1 + x
        y = y - 1
    return round(x, 2)

print(bank(n, years))