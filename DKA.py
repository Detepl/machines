import json

with open('DKA.txt') as json_file:
    avtomat = json.load(json_file)

chain = [int(j) for j in input("Введите цепочку - ").split()]


def test(table, alphabet, chain):
    for k in chain:
        if k not in alphabet:
            print("В введённой цепочке есть неправильный символ - ", k)
            return 0

    mas = [i for i in range(0, len(table))]
    for k in table:
        if len(table[k]) != len(alphabet):
            print("В таблице переходов указаны не все пути")
            return 0

        try:
            a = int(k[1:])
        except:
            print("ошибка в", k, table[k], "в", k)
            return 0

        if a == mas[0]:
            mas.pop(0)
        else:
            print("ошибка в", k, table[k], "в", k)
            return 0

        for i in table[k]:
            if i not in table:
                print("ошибка в", k, table[k], "в таблице переходов нет", i)
                return 0

    if len(mas) == 0:
        return 1
    else:
        return 0


if test(avtomat["table"], avtomat["alphabet"], chain) == 0:
    quit()
else:
    print("все проверки пройденны")

position_now = "q0"
for k in chain:
    position_now = avtomat["table"][position_now][k]

if position_now in avtomat["allowing positions"]:
    print("допускает")
else:
    print("не допускает")











