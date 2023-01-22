import json

# машина прибавит к двоичной последовательности 1
machine = {

    "start": 0,

    "allowing_pos": [3],

    "alphabet": ["", "0", "1"],

    "data": [{'': {'write': '', 'move': 'L', 'jump': 1}, '0': {'write': '', 'move': 'R', 'jump': 0},'1': {'write': '', 'move': 'R', 'jump': 0}},
             {'': {'write': '1', 'move': 'N', 'jump': 3}, '0': {'write': '1', 'move': 'N', 'jump': 3},'1': {'write': '0', 'move': 'L', 'jump': 2}},
             {'': {'write': '1', 'move': 'N', 'jump': 3}, '0': {'write': '1', 'move': 'N', 'jump': 3},'1': {'write': '0', 'move': 'L', 'jump': 2}}],

}

with open('machine.txt', 'w') as outfile:
    json.dump(machine, outfile)
