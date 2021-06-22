def pocket_analysis(filename):
    #read in
    data = open(filename)
    #count number of pockets
    num_case = 1

    data_list = []
    for line in data:
        num_case += 1
        data_list.append(str(line))
    num_pocket = int(num_case/21)

    #outer loop with number of pockets
    res = []
    for i in range(num_pocket):
        row = []
        for j in range(1, 20):
        #split with : delimiter
            info = data_list[i * 21 + j]
            temp = info.split(":")
            item = temp[1]
            #take out /t /n
            item = item[item.find('\t')+1:item.find('\n')]
            row.append(float(item))
        res.append(row)
    #return the list
    return res
