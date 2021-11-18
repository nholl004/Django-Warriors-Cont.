from types import NoneType
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .forms import serverForm
from .models import search
# Create your views here.

caseList = [[]]
line_count = 0
import_cnt = 0
def importButton(request):
    global import_cnt
    importFunction()
    return render(request, 'server_view/import.html')

def importFunction():
    global line_count 
    global caseList

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
            #print(tmp,new_line)
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
        # print(infoList)
        line_count += 1
    tmp_list.pop(0)
    caseList = tmp_list
    print('case size:',len(caseList))
print('case size:',len(caseList))

def search(request):
    global line_count 
    global caseList

    searched_data = request.POST.get('search')
    #print(searched_data)
    x = 0
    data_info = [[]]
    #print(data_info)
    if (searched_data != None):
        while( x != line_count-1):
            x += 1
            for y in range(8):
                if(caseList[x][y].lower() == searched_data.lower()):
                    data_info.append(caseList[x])

    #print(len(data_info))
    if (len(data_info)<2):
        error = True
        return render(request,'server_view/search.html', {'searched':searched_data, 
        'error':error})
        #print(data_info)
    else:
        error = False
        data_info.pop(0)
        #print(data_info)
        return render(request,'server_view/search.html', {'searched':searched_data,
        'data_info':data_info,'error':error})

def top_cases(request):
    global caseList
    tmp = caseList
    list = []
    conf = []
    prov = []
    
    for i in range(1,len(tmp)): 
        k =0
        k1 = 0
        k1_2cnt = 0
        if(tmp[i][2] != ''):
            if(len(list)==0):
                list.append(tmp[i])
            else:
                cnt = 0
                for x in range(0,len(list)):
                    if(list[x][2]==tmp[i][2]):
                        cnt +=1
                        if(float(list[x][5])<=float(tmp[i][5])):
                            list[x] = tmp[i]
                if(cnt == 0):
                    for l in range(0,len(list)):
                        if(len(list)==10):                          
                            if(float(list[l][5])<=float(tmp[i][5])):
                                k = l  
                                k1_2cnt = 1      
                            else:
                                k1 = 2                       
                        elif(len(list)<10):
                            k1 = 1
                    if(k1 == 1):
                        list.append(tmp[i])
                    elif(k1_2cnt == 1):
                        list[k] = tmp[i]
        

    for fill in list:#fills values for graph
        conf.append(fill[5])
        prov.append(fill[2])
    return render(request, 'server_view/top_cases.html',{'data_info':list,
    'conf':conf,'prov':prov})    

def top_deaths(request):
    global caseList
    tmp = caseList
    list = []
    deaths = []
    prov = []

    for i in range(1,len(tmp)): 
        k =0
        k1 = 0
        k1_2cnt = 0
        if(tmp[i][2] != ''):
            if(len(list)==0):
                list.append(tmp[i])
            else:
                cnt = 0
                for x in range(0,len(list)):
                    if(list[x][2]==tmp[i][2]):
                        cnt +=1
                        if(float(list[x][6])<=float(tmp[i][6])):
                            list[x] = tmp[i]
                if(cnt == 0):
                    for l in range(0,len(list)):
                        if(len(list)==10):                          
                            if(float(list[l][6])<=float(tmp[i][6])):
                                k = l  
                                k1_2cnt = 1      
                            else:
                                k1 = 2                       
                        elif(len(list)<10):
                            k1 = 1
                    if(k1 == 1):
                        list.append(tmp[i])
                    elif(k1_2cnt == 1):
                        list[k] = tmp[i]
    for fill in list:#fills values for graph
        deaths.append(fill[6])
        prov.append(fill[2])
    #print(list)
    return render(request, 'server_view/top_deaths.html',{'data_info':list,
    'deaths':deaths,'prov':prov})    


def top_recov(request):
    global caseList
    tmp = caseList
    list = []
    recov = []
    prov = []

    for i in range(1,len(tmp)): 
        k =0
        k1 = 0
        k1_2cnt = 0
        if(tmp[i][2] != ''):
            if(len(list)==0):
                list.append(tmp[i])
            else:
                cnt = 0
                for x in range(0,len(list)):
                    if(list[x][2]==tmp[i][2]):
                        cnt +=1
                        if(float(list[x][7])<=float(tmp[i][7])):
                            list[x] = tmp[i]
                if(cnt == 0):
                    for l in range(0,len(list)):
                        if(len(list)==10):                          
                            if(float(list[l][7])<=float(tmp[i][7])):
                                k = l  
                                k1_2cnt = 1      
                            else:
                                k1 = 2                       
                        elif(len(list)<10):
                            k1 = 1
                    if(k1 == 1):
                        list.append(tmp[i])
                    elif(k1_2cnt == 1):
                        list[k] = tmp[i]
    for fill in list:#fills values for graph
        recov.append(fill[7])
        prov.append(fill[2])

    return render(request, 'server_view/top_recov.html',{'data_info':list,
    'recov':recov,'prov':prov})    


def backup(request):
    #make a copy of current data 
    #parse the current data into another csv file 
    test_file = open("covid_19_data.csv", "w")
    line = ''
    for x in caseList:
        for y in range(0,8):
            line += x[y]
            if(y < 7):
                line += ','
    test_file.write(line)
    test_file.close()
    return render(request, 'server_view/backup.html')
    

#This function Deletes the data at the specific SNo value.
#This value is obtained in /search url and requires user input.     
def delete(request):
    delete_index = str(request.POST.get('index'))
    cnt = 0
    data = 0
    #print(delete_index)
    
    #print(caseList[1:5])
    if(delete_index == 'None'):
        #print('hi')
        return render(request,'server_view/delete.html')
    elif(delete_index != 'None'):
        #print(caseList[306426:])
        for i in range(1,len(caseList)-1):
            if(int(caseList[i][0]) == int(delete_index)):
                cnt += 1
                data = caseList[i]
                caseList.pop(i)

        #allows us to delete last value
            elif(int(caseList[len(caseList)-1][0]) == int(delete_index)):
                cnt+=1
                data = caseList[len(caseList)-1]
                caseList.pop(len(caseList)-1)
        if(cnt==0):
            data = 'No such index'
        #print(caseList[306426:])
        return render(request,'server_view/delete.html',{'del_data':data})

#This functions reads 7 user inputs after submit button pressed or enter
#If inputs are filled minus state/province it is saved in to csv file
def insert(request):
    tmp_file = []
    Sno1 = int(caseList[len(caseList)-1][0])+1
    observ1 = str(request.POST.get('observ'))
    state1 = str(request.POST.get('state'))
    state1 = '\"' + state1 + '\"'
    country1 = str(request.POST.get('country'))
    lastUp1 = str(request.POST.get('lastUp'))
    confirms1 = str(request.POST.get('confirm'))
    deaths1 = str(request.POST.get('deaths'))
    recovered1 = str(request.POST.get('recover'))
    recovered1 = recovered1 + '\n'#preps for save to file

    if not observ1 or not country1 or not lastUp1 or not confirms1 or not deaths1 or not recovered1:
        error = True
        return render(request,'server_view/insert.html',{'error':error,'observ':observ1,'state':state1,'country':country1,
    'lastUp':lastUp1,'confirms':confirms1,'deaths':deaths1,'recovered':recovered1})
    else:
        error = False
        
        tmp_file.append(str(Sno1)) 
        tmp_file.append(observ1)
        tmp_file.append(state1)
        tmp_file.append(country1)
        tmp_file.append(lastUp1)
        tmp_file.append(confirms1)
        tmp_file.append(deaths1)
        tmp_file.append(recovered1)
        caseList.append(tmp_file)

        if(str(caseList[len(caseList)-1][1]) == "None"):
            caseList.pop(len(caseList)-1)

        return render(request,'server_view/insert.html',{'error':error,'observ':observ1,'state':state1,'country':country1,
    'lastUp':lastUp1,'confirms':confirms1,'deaths':deaths1,'recovered':recovered1})

# This update feature, is able to update the current data structure with input of strings. 
# Given the index, we can update the row to which the data is inputted. Similar to that of insert. 


def update(request):

    indexToUpdate = str(request.POST.get('index'))
    confirms2 = str(request.POST.get('confirm'))
    deaths2 = str(request.POST.get('deaths'))
    recovered2 = str(request.POST.get('recover'))

    if not indexToUpdate or not confirms2 or not deaths2 or not recovered2:
        error = True
        return render(request,'server_view/update.html',{'error':error,'index':indexToUpdate,'confirms':confirms2,'deaths':deaths2,'recovered':recovered2})
    else:
        error = False

        if(indexToUpdate == 'None'):
            return render(request,'server_view/update.html')
        else:
            for i in range(1,len(caseList)-1):
                if(int(caseList[i][0]) == int(indexToUpdate)):                  
                    caseList[i][5] = str(confirms2+'.0')
                    caseList[i][6] = str(deaths2+'.0')
                    caseList[i][7] = str(recovered2+'.0\n')
                    print(caseList[i-2:i+4])
                else:
                    error = True

        return render(request,'server_view/update.html',{'error':error,'index':indexToUpdate,'confirms':confirms2,'deaths':deaths2,'recovered':recovered2})

def confirm_to_death(request):
    global caseList
    serialNo = str(request.POST.get('SN'))
    contextTmp = []
    context = []
    if not serialNo:
        print(3)
        error = True
        return render(request,'server_view/confirmtodeath.html',{'error':error,'data_info': context })
    else:
        error = False
        if(serialNo == 'None'):
            return render(request,'server_view/confirmtodeath.html')
        ratio = -1; 
        for i in range(1, len(caseList) - 1):
            if(int(caseList[i][0]) == int(serialNo)):
                casesConfirmed = float(caseList[i][5])
                casesDeaths = float(caseList[i][6])
                if(casesDeaths == 0):
                    casesDeaths = 1
                # confirmed / deaths
                ratio = casesConfirmed / casesDeaths
                # contextTmp.append(float(casesConfirmed))
                # contextTmp.append(float(casesDeaths))
                # contextTmp.append(float(ratio))
                contextTmp.append(casesConfirmed)
                contextTmp.append(casesDeaths)
                contextTmp.append(ratio)
                
                context.append(contextTmp)
                # context["confirmedDeaths"] = str(casesDeaths)
                # context["ratio"] = ratio 
                print(ratio)
                return render(request,'server_view/confirmtodeath.html', {'data_info':context})
            else:
                error = True;    

    #return render(request,'server_view/confirmtodeath.html',{'error':error,'SN':serialNo })
      
# Function shows the recovery rate in each city
# Confirmed / recovered
# should be recovered / confirmed (* 100)
def rec_Rate(request):

    global caseList
    rec_tmp = caseList
    tmp_list = []
    rec_list = []
    rate = 0.0
    currDay = 1

    recoveredNum = 0
    recoveredHigh = 0
    recoveredLow = 0
    
    confirmedDenom = 0
    confirmedHigh = 0
    confirmedLow = 0

    month = request.POST.get('month')
    year = request.POST.get('year')
    state = request.POST.get('location')

    for line in range(1,len(caseList)-1):
        splitInput = split_date(caseList[line][1]) # 01/02/2020
        if (splitInput[1][0] == '0'):
            tmpDay = int(splitInput[1][1])
        else:
            tmpDay = int (splitInput[1])
        
        if(splitInput[0] == month and splitInput[2] == year and currDay <= 31 and caseList[line][2] == state):
            currDay+=1
            if (splitInput[2] == '2021' and month == '05'):
                if (tmpDay == 29):
                    recoveredHigh = float(rec_tmp[line][7])
                    confirmedHigh = float(rec_tmp[line][5])
                elif (tmpDay == 1):
                    recoveredHigh = float(rec_tmp[line][7])
                    confirmedHigh = float(rec_tmp[line][5])
            if (month == '01' or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12'):
                if (tmpDay == 31):
                    recoveredHigh = float(rec_tmp[line][7])
                    confirmedHigh = float(rec_tmp[line][5])
                elif (tmpDay == 1):
                    recoveredLow = float(rec_tmp[line][7])
                    confirmedHigh = float(rec_tmp[line][5])
            if (month == '02'):
                if (tmpDay == 28 or tmpDay == 29):
                    recoveredHigh = float(rec_tmp[line][7])
                    confirmedHigh = float(rec_tmp[line][5])
                elif (tmpDay == 1):
                    recoveredLow = float(rec_tmp[line][7])
                    confirmedHigh = float(rec_tmp[line][5])
            if (month == '04' or month == '06' or month == '09' or month == '11'):
                if (tmpDay == 30):
                    recoveredHigh = float(rec_tmp[line][7])
                    confirmedHigh = float(rec_tmp[line][5])
                elif (tmpDay == 1):
                    recoveredLow = float(rec_tmp[line][7])
                    confirmedHigh = float(rec_tmp[line][5])
    
    recoveredNum = recoveredHigh - recoveredLow
    confirmedDenom = confirmedHigh - confirmedLow
            
    if (confirmedDenom == 0.0):
        rate = 0.0
    else:
        tmp = (recoveredNum / confirmedDenom) * 100
        rate = "{:.2f}".format(tmp)
        # rec_list[line][0] = rec_tmp[line][2]
        
    tmp_list.append(state) #state/province
    tmp_list.append(rate)
    rec_list.append(tmp_list)
    # print(tmp_list[])
    tmp_list = []

    return render(request, 'server_view/recRate.html',{'data_info':rec_list})

# deaths / (deaths + recovered) * 100 <- refers to ongoing epidemic
# nonongoing cfr is deaths / confirmed * 100 
# case fatality ratio is the proportion of individuals diagnosed with a disease who die from that disease and is therefore a measure of severity among detected cases
def caseFatalityRatio(request):
    
    global caseList
    case_tmp = caseList
    rate = 0.0
    newList = []
    ratioList = []

    for i in range (1, len(case_tmp) - 1):
        if (float(caseList[i][6]) + float (caseList[i][7]) == 0):
            ratio = 0.0
        else:
            ratioTmp = ((float(caseList[i][6]) / (float(caseList[i][6]) + float(caseList[i][7]))) * 100)
            ratio = "{:.2f}".format(ratioTmp)

        newList.append(caseList[i][2])
        newList.append(caseList[i][3])
        newList.append(ratio)
        ratioList.append(newList)
        newList = [] #empty list for next iteration

    return render(request, 'server_view/caseFatality.html', {'data_info': ratioList})
    

def daily_cases(request):
    #sort the cases of a certain location and month
    month = request.POST.get('month')
    year = request.POST.get('year')
    location = request.POST.get('location') #gets province/state
    
    #find the beginning of the month aka the first
    #keep iterating until 28 days are iterated through
    #a valid row is when month year current day and location are correct

    dailyCasesList = []
    currDay = 1

    

    for i in range(1, len(caseList) - 1):
        splitList = split_date(caseList[i][1]) #split into 3  strings of "mm" "dd" "YYYY"
        #convert the day to an integer
        if(splitList[1][0] == '0'): #if first character in "dd" is 0 then convert second character to int
            tmpDay = int(splitList[1][1])
        else:
            tmpDay = int(splitList[1])

        if(splitList[0] == month and currDay == tmpDay and currDay <= 31 and splitList[2] == year and caseList[i][2] == location ):
            #add valid row to list
            dailyCasesList.append(caseList[i][0:6])
            currDay = currDay + 1
            
    # print(dailyCasesList[0:-1])
    # print(currDay)
    return render(request, 'server_view/daily.html', {'data_info':dailyCasesList})

def daily_deaths(request):
    #sort the cases of a certain location and month
    month = request.POST.get('month')
    year = request.POST.get('year')
    location = request.POST.get('location') #gets province/state
    
    #find the beginning of the month aka the first
    #keep iterating until 28 days are iterated through
    #a valid row is when month year current day and location are correct

    dailyCasesList = []
    currDay = 1

    

    for i in range(1, len(caseList) - 1):
        splitList = split_date(caseList[i][1]) #split into 3  strings of "mm" "dd" "YYYY"
        #convert the day to an integer
        if(splitList[1][0] == '0'): #if first character in "dd" is 0 then convert second character to int
            tmpDay = int(splitList[1][1])
        else:
            tmpDay = int(splitList[1])

        if(splitList[0] == month and currDay == tmpDay and currDay <= 31 and splitList[2] == year and caseList[i][2] == location ):
            #add valid row to list
            caseListCombined = caseList[i][0:5] + caseList[i][6:7]
            dailyCasesList.append(caseListCombined)
            currDay = currDay + 1
            
    # print(dailyCasesList[0:-1])
    # print(currDay)
    return render(request, 'server_view/daily_deaths.html', {'data_info':dailyCasesList})

        

def split_date(date):    
    #mm/dd/yyyy
    #0123456789
    month = date[0:2]
    day = date[3:5]
    year = date[6:10]
    dateList = [month,day,year]
    return dateList

# Comparing 2 States/Provinces: Graph Edition
def compareTwo(request):
    global caseList
    conf1 = 0
    conf2 = 0
    death1 = 0
    death2 = 0
    rec1 = 0
    rec2 = 0

    state1 = str(request.POST.get('SP1'))
    state2 = str(request.POST.get('SP2'))
    # print("about to go into the if\n")

    if state1 == '' or state2 == '':
        # print("in if \n")
        error = True
        return render(request, 'server_view/compare.html',{'error':error, 'state1':state1, 'state2':state2, 'conf1':conf1, 'death1':death1, 'rec1':rec1, 'conf2':conf2, 'death2':death2, 'rec2':rec2, })

    elif (int(caseList[305665][0]) >= 305665):
        # print("in else if\n")
        error = False
        for line in range(305665,len(caseList)):
            if (caseList[line][2].lower() == state1.lower()):
                state1 = caseList[line][2]
                # print("found \n", state1)
                # cases.append(caseList[line][5])
                # cases.append(caseList[line][6])
                # cases.append(caseList[line][7])
                conf1 = caseList[line][5]
                death1 = caseList[line][6]
                rec1 = caseList[line][7]
            if (caseList[line][2].lower() == state2.lower()):
                state2 = caseList[line][2]
                conf2 = caseList[line][5]
                death2 = caseList[line][6]
                rec2 = caseList[line][7]
                # cases2.append(caseList[line][5])
                # cases2.append(caseList[line][6])
                # cases2.append(caseList[line][7])
                # print(conf2 +  " " + death2 + " " + rec2))
        return render(request, 'server_view/compare.html',{'error':error, 'state1':state1, 'state2':state2, 'conf1':conf1, 'death1':death1, 'rec1':rec1, 'conf2':conf2, 'death2':death2, 'rec2':rec2, })
    else:
        # print("in else\n")
        error = False
    # print("about to end\n")
        return render(request, 'server_view/compare.html',{'error':error, 'state1':state1, 'state2':state2, 'conf1':conf1, 'death1':death1, 'rec1':rec1, 'conf2':conf2, 'death2':death2, 'rec2':rec2, })

def peakdays(request):
    HighestPeakDiffConfirmed = 0 #index 6 for confirmed
    HighestPeakDiffDeaths = 0 #index 7 for deaths
    HighestPeakDiffRecovered = 0 #index 8 for recovered
    DateOfHighestPeakConfirmed = ""
    DateOfHighestPeakDeaths = ""
    DateOfHighestPeakRecovered = ""
    specificLocationList = []
    tmpList = []
    contexts = {}
    Province_State = str(request.POST.get('Prov/State'))
    Country_Region = str(request.POST.get('Country/Region'))

    #parsing the current caselist [[]] to a more specific.
    #for line in range(1, len(caseList) - 1):

    print(Province_State)
    print(Country_Region)
    for i in range(1,len(caseList)-1):
        if(caseList[i][3] == Country_Region and caseList[i][2] == Province_State):
            for y in range(0,8):
                tmpList.append(caseList[i][y])
            specificLocationList.append(tmpList)
            tmpList = []
    #for k in range(1,len(specificLocationList)-1):
    #    print(specificLocationList[k][6])
    #Gathering peak data for confirmed cases.
    for j in range(2,len(specificLocationList)-1):
        if(float(specificLocationList[j][5]) - float(specificLocationList[j - 1][5]) > HighestPeakDiffConfirmed):
            HighestPeakDiffConfirmed = float(specificLocationList[j][5]) - float(specificLocationList[j - 1][5])
            DateOfHighestPeakConfirmed = specificLocationList[j][1]
    contexts["confirmedCase"] = str(HighestPeakDiffConfirmed)
    contexts["confirmedCaseDate"] = str(DateOfHighestPeakConfirmed)
    #Gathering peak data for death cases.
    for j in range(2,len(specificLocationList)-1):
        if(float(specificLocationList[j][6]) - float(specificLocationList[j - 1][6]) > HighestPeakDiffDeaths):
            HighestPeakDiffDeaths = float(specificLocationList[j][6]) - float(specificLocationList[j - 1][6])
            DateOfHighestPeakDeaths = specificLocationList[j][1]
    contexts["deathCase"] = str(HighestPeakDiffDeaths)
    contexts["deathCaseDate"] = str(DateOfHighestPeakDeaths)
    #Gathering peak data for recovered cases.
    for j in range(2,len(specificLocationList)-1):
        if(float(specificLocationList[j][7]) - float(specificLocationList[j - 1][7]) > HighestPeakDiffRecovered):
            HighestPeakDiffRecovered = float(specificLocationList[j][7]) - float(specificLocationList[j - 1][7])
            DateOfHighestPeakRecovered = specificLocationList[j][1]
    contexts["recoveredCase"] = str(HighestPeakDiffRecovered)
    contexts["recoveredCaseDate"] = str(DateOfHighestPeakRecovered)


    return render(request, 'server_view/peakdays.html', contexts)
