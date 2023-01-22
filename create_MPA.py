import json

#допускает цепочки состоящие из равного кол-ва 1 и 0
avtomat = {
    "alphabet": ["0", "1"],

    "allowing positions": [],

    #после указания перехода на след состояние, указывается массив с заменами верха стэка
    #["F", "0F"] - если наверху F, то меняется на 0F
    "table": {
        'q0': [["q0", [["F", "0F"], ["1", None], ["0", "00"]]], ["q0", [["F", "1F"], ["0", None], ["1", "11"]]]]}
}

with open('MPA.txt', 'w') as outfile:
    json.dump(avtomat, outfile)