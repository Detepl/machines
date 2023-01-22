import json

with open('MPA2.txt') as json_file:
    avtomat = json.load(json_file)

chain = []
s = input()
for i in s:
    chain.append(avtomat["alphabet"].index(i))

stack = "F"

positions_now = ["q0"]

for k in chain:
    new_positions = []
    for i in positions_now:
        for j in avtomat["table"][i][k][1:]:
            new_positions.append(avtomat["table"][i][k][0])
            for f in j:
                if f[0] == stack[-1]:
                    if f[1] == None:
                        stack = stack[:-1]
                    else:
                        stack = stack[:-1] + f[1][::-1]

                    break

    positions_now = new_positions.copy()


def allowing_test(pos, allow_pos):
    for i in pos:
        if i in allow_pos:
            return 1
            break
    return 0


if allowing_test(positions_now, avtomat["allowing positions"]) == 1 or stack == "F":
    print("допускает")
else:
    print("не допускает")

