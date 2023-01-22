import json

with open('DKA.txt') as json_file:
    avtomat = json.load(json_file)


equival_table=[[0 for j in range(0,i)]for i in range(1,len(avtomat["table"]))]

#шаг 1 (тут в таблице обозначаются эквивалентными
#все пары состоящие из допускающих состояний)
def check_equival(node1,node2):
    if node1 in avtomat["allowing positions"] and node2 in avtomat["allowing positions"]:
        return 0
    else:
        if node1 in avtomat["allowing positions"] or node2 in avtomat["allowing positions"]:
            return 1
        else:
            return 0

for i in range(0,len(avtomat["table"])-1):
    for j in range(0,i+1):
        if check_equival("q"+str(i+1),"q"+str(j))==1:
            equival_table[i][j]=1


#шаг 2 (в таблице вычисляются все эквивалентные пары)
#2 раза проходимся по таблице, и если пара ведёт
#в неэквивалентную пару, то она неэквивалентна           
for k in range(0,2):
    for i in range(0,len(avtomat["table"])-1):
        for j in range(0,i+1):
            
            if equival_table[i][j]==0 and ("q"+str(i+1)) not in avtomat["allowing positions"] and ("q"+str(j)) not in avtomat["allowing positions"]:
                equivalence=0
                
                for char in avtomat["alphabet"]:
                    i1=int(avtomat['table']["q"+str(i+1)][char][1:])-1
                    j1=int(avtomat['table']["q"+str(j)][char][1:])

                    if i1<j1:
                        i1,j1=j1-1,i1+1
                        
                    if equival_table[i1][j1]==1:
                        equivalence=1
                        break
                    
                if equivalence==1:
                    equival_table[i][j]=1



#шаг 3
#проходимся по таблице и собираем уникальные состояния
not_used = [i for i in range(0,len(equival_table)+1)]
final={}
equal_pos = []

for i in range(len(avtomat["table"])-2,-1,-1):
    
    if i+1 in not_used:
        not_used.remove(i+1)
        new_pos = ["q"+str(i+1)]
        final.update({"q"+str(i+1):"q"+str(i+1)})
        for j in range(0,len(equival_table[i])):
            
            if equival_table[i][j] == 0 and j in not_used:
                not_used.remove(j)
                pos = {"q"+str(j):"q"+str(i+1)}
                final.update(pos)

                new_pos.append("q"+str(j))
        equal_pos.append(new_pos)
                


#шаг 4 (собираем минимизированный ДКА)
min_DKA = {
    "alphabet":[],
    
    "allowing positions":[],
    
    "table":{
      'q0' : [],}
    }

min_DKA.update({"alphabet":avtomat["alphabet"]})


num_q = 0
new_allowing_pos = []
for i in equal_pos:

    old_way = avtomat["table"][i[0]]
    #строим новую строчку перехода в table
    for j in range(0,len(equal_pos)):
        if final[old_way[0]] in equal_pos[j]:
            pos0 = j
                 
        if final[old_way[1]] in equal_pos[j]:
            pos1 = j
            
        #находим новые допускающие состояния
        for p in avtomat["allowing positions"]:
            if p in equal_pos[j] and "q"+str(j) not in new_allowing_pos:
                new_allowing_pos.append("q"+str(j))
                
        
            
    new_way = {"q"+str(num_q):["q"+str(pos0),"q"+str(pos1)]}

    min_DKA["table"].update(new_way)

    num_q = num_q + 1

new_allowing_pos = {"allowing positions":new_allowing_pos}
min_DKA.update(new_allowing_pos)


with open('min_DKA.txt', 'w') as outfile:
    json.dump(min_DKA, outfile)

