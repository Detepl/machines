import json

with open('NKA.txt') as json_file:
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
            for j in i:
                if j not in table:
                    print("ошибка в", k, table[k], "в таблице переходов нет", j)
                    return 0

    if len(mas) == 0:
        return 1
    else:
        return 0


if test(avtomat["table"], avtomat["alphabet"], chain) == 0:
    quit()
else:
    print("все проверки пройденны")

positions_now = ["q0"]
for k in chain:
    new_positions = []
    for i in positions_now:  # перебор текущих состояний
        for j in avtomat["table"][i][k]:  # перебор переходов из текущих состояний
            new_positions.append(j)

    positions_now = new_positions.copy()


def allowing_test(pos, allow_pos):
    for i in pos:
        if i in allow_pos:
            return 1
            break
    return 0


if allowing_test(positions_now, avtomat["allowing positions"]) == 1:
    print("допускает")
else:
    print("не допускает")
