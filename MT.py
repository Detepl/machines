import json


def test_machine(machine):
    if machine['start'] == None:
        print("отсутсвует начальное положение")
        return 0
    if machine['allowing_pos'] == None:
        print("отсутсвует допускающее положение")
        return 0

    for i in machine["data"]:

        for j in i:

            if j not in machine['alphabet']:
                print("недопустимый символ", j)
                return 0

            if i[j]['write'] not in machine['alphabet']:
                print("недопустимый символ", i[j]['write'])
                return 0

            if i[j]['move'] == "N" or i[j]['move'] == "R" or i[j]['move'] == "L":
                a = 3
            else:
                print("недопустимый символ", i[j]['move'])
                return 0

            if type(i[j]['jump']) != int:
                print("недопустимый символ", i[j]['jump'])
                return 0

    return 1


def run_machine(machine, chain):
    position_now = machine['start']

    lane = [c for c in chain]

    empty = machine['alphabet'][0]
    pos_reader = 0

    while True:

        comms = machine['data'][position_now][lane[pos_reader]]

        if comms['write']:
            lane[pos_reader] = comms['write']

        if comms['move'] == 'R':
            pos_reader += 1
            if pos_reader == len(lane):
                lane += [empty]



        elif comms['move'] == 'L':
            pos_reader -= 1
            if pos_reader == -1:
                lane = [empty] + lane

                pos_reader = 0

        position_now = comms['jump']

        if position_now in machine['allowing_pos']:
            break

    return ''.join(lane)


with open('machine.txt', 'r') as json_file:
    machine = json.load(json_file)

if test_machine(machine) == 1:
    print(run_machine(machine, "111"))
