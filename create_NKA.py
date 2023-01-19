import json
avtomat = {
    "alphabet": [0, 1],

    "allowing positions": ["q1"],

    "table": {
        'q0': [['q0'], ['q0', 'q1']], #допускает цепочки которые заканиваются на 1
        'q1': [[], []]}
}

with open('NKA.txt', 'w') as outfile:
    json.dump(avtomat, outfile)