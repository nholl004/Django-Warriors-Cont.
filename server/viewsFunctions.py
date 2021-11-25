def test():
    print("viewsFunction file working... ")

def importFunc():
    tmp_list = [[]]
    csv_file = open("covid_19_data.csv")
    
    for line in csv_file:
        infoList = []
        infoList = line.split(',')
        tmp = []
        tmp1 = []
        new_line = ''
        if(len(infoList)>8):#fixes provice split issue
            tmp = infoList[2:len(infoList)-5]
            for x in range(len(tmp)):
                new_line += tmp[x]
                if(x < len(tmp)-1):
                    new_line += ', '

            tmp1.append(infoList[0])
            tmp1.append(infoList[1])
            tmp1.append(new_line)
            tmp1.append(infoList[(len(infoList)-5)])
            tmp1.append(infoList[(len(infoList)-4)])
            tmp1.append(infoList[(len(infoList)-3)])
            tmp1.append(infoList[(len(infoList)-2)])
            tmp1.append(infoList[(len(infoList)-1)])
            infoList = tmp1
        tmp_list.append(infoList)
    tmp_list.pop(0)
    tmp_list
    print('case size:',len(tmp_list))
    return tmp_list

def top10(data_position,database_list):
    list = []
    for i in range(1,len(database_list)): 
        k =0
        k1 = 0
        k1_2cnt = 0
        
        if(database_list[i][2] != '' and database_list[i][2] != 'Recovered'):
            if(len(list)==0):
                list.append(database_list[i])
            else:
                cnt = 0
                for x in range(0,len(list)):
                    if(list[x][2]==database_list[i][2]):
                        cnt +=1
                        if(float(list[x][data_position])<=float(database_list[i][data_position])):
                            list[x] = database_list[i]
                if(cnt == 0):
                    for l in range(0,len(list)):
                        if(len(list)==10):                          
                            if(float(list[l][data_position])<=float(database_list[i][data_position])):
                                k = l  
                                k1_2cnt = 1      
                            else:
                                k1 = 2                       
                        elif(len(list)<10):
                            k1 = 1
                    if(k1 == 1):
                        list.append(database_list[i])
                    elif(k1_2cnt == 1):
                        list[k] = database_list[i]
    return list
    
def caseTotal(data_position,database_list):
    sum = 0
    list = []
    for i in range(1,len(database_list)):
        if(database_list[i][2] != ''):
            if(sum == 0):
                sum += float(database_list[i][data_position])
                list.append(database_list[i])
            else:
                k = 0
                for x in range(1,len(list)):
                    if(list[x][2]==database_list[i][2] and float(list[x][data_position]) <= float(database_list[i][data_position])):
                        sum -= float(list[x][data_position])
                        sum += float(database_list[i][data_position])
                    
                        k = x
                if(k == 0):
                    sum += float(database_list[i][data_position]) 
                else:
                    list.append(database_list[i]) 
                    list.pop(k)

    return sum