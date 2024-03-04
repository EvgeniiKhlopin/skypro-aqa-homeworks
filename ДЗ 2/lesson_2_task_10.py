def bank(x, y):
    balance = x
    for _ in range(y):
        balance += balance * 0.1
    return balance

x = int(input("Введите сумму вклада: "))
y = int(input("Введите срок вклада (количество лет): "))
result = bank(x, y)
print("Сумма денег на вкладе через", y, "лет:", result)