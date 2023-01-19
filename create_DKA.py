import json

avtomat = {
    "alphabet": [0, 1],

    #допускающие состояния
    "allowing positions": ["q0"],

    #таблица переходов
    "table": {
        'q0': ['q1', 'q3'],
        'q1': ['q0', 'q2'],   #допускает цепочки состоящие из чётного
        'q2': ['q1', "q3"],   #кол-ва 0 и 1
        'q3': ['q2', 'q0'],}
}

with open('DKA.txt', 'w') as outfile:
    json.dump(avtomat, outfile)
