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
                if(caseList[x][y][0:5] == searched_data or caseList[x][y].lower() == searched_data.lower()):
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
    list = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0]]
    conf = []
    prov = []

    for i in range(1,len(tmp)): 
        k =0
        if(tmp[i][2] != ''):
            for j in range(0,10): # checks to make sure no duplicate states. Takes the greatest value.  
                for x in range(0,10):
                    if(list[j][2]==list[x][2]):
                        if(float(list[j][5])<float(list[x][5])):
                            list.pop(j)
                            list.append([0,0,0,0,0,0,0,0])
            for l in range(0,10):#finds the lowest value
                if(float(list[l][5])<=float(list[k][5])):
                    k = l 
            if(float(list[k][5])<float(tmp[i][5])):#pops lowest value if new found value is greater
                list.pop(k)
                list.append(tmp[i])
    for fill in list:#fills values for graph
        conf.append(fill[5])
        prov.append(fill[2])
    return render(request, 'server_view/top_cases.html',{'data_info':list,
    'conf':conf,'prov':prov})    

def top_deaths(request):
    global caseList
    tmp = caseList
    list = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0]]
    deaths = []
    prov = []

    for i in range(1,len(tmp)): 
        k =0
        if(tmp[i][2] != ''):
            for j in range(0,10): # checks to make sure no duplicate states. Takes the greatest value.  
                for x in range(0,10):
                    if(list[j][2]==list[x][2]):
                        if(float(list[j][6])<float(list[x][6])):
                            list.pop(j)
                            list.append([0,0,0,0,0,0,0,0])
            for l in range(0,10):#finds the lowest value
                if(float(list[l][6])<=float(list[k][6])):
                    k = l 
            if(float(list[k][6])<float(tmp[i][6])):#pops lowest value if new found value is greater
                list.pop(k)
                list.append(tmp[i])
    for fill in list:#fills values for graph
        deaths.append(fill[6])
        prov.append(fill[2])
    #print(list)
    return render(request, 'server_view/top_deaths.html',{'data_info':list,
    'deaths':deaths,'prov':prov})    


def top_recov(request):
    global caseList
    tmp = caseList
    list = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0]]
    recov = []
    prov = []

    for i in range(1,len(tmp)): 
        k =0
        if(tmp[i][2] != ''):
            for j in range(0,10): # checks to make sure no duplicate states. Takes the greatest value.  
                for x in range(0,10):
                    if(list[j][2]==list[x][2]):
                        if(float(list[j][7])<float(list[x][7])):
                            list.pop(j)
                            list.append([0,0,0,0,0,0,0,0])
            for l in range(0,10):#finds the lowest value
                if(float(list[l][7])<=float(list[k][7])):
                    k = l 
            if(float(list[k][7])<float(tmp[i][7])):#pops lowest value if new found value is greater
                list.pop(k)
                list.append(tmp[i])
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

def ConfirmToDeath(request):
    serialNo = str(request.POST.get('SN'))
    context = {}
    if not serialNo:
        error = True
        return render(request,'server_view/confirmtodeath.html',{'error':error,'SN':serialNo })
    else:
        error = False
        if(serialNo == 'None'):
            return render(request,'server_view/confirmtodeath.html')
        ratio = -1; 
    
        for i in range(1,len(caseList) - 1):
            if(int(caseList[i][0]) == int(serialNo)):
                casesConfirmed = float(caseList[i][5])
                casesDeaths = float(caseList[i][6])
                if(casesDeaths == 0):
                    casesDeaths = 1
                ratio = casesConfirmed / casesDeaths
                context["confirmedCases"] = str(casesConfirmed)
                context["confirmedDeaths"] = str(casesDeaths)
                
                context["ratio"] = ratio 
                print(ratio)
                return render(request,'server_view/confirmtodeath.html',context, {'error':error,'SN':serialNo})
            else:
                error = True;    

    #return render(request,'server_view/confirmtodeath.html',{'error':error,'SN':serialNo })
      
# Function shows the recovery rate in each city
# Confirmed / recovered
def rec_Rate(request):

    global caseList
    rec_tmp = caseList
    tmp_list = []
    rec_list = []
    rate = 0.0

    for line in range(1,len(caseList)-1):
        if (float(rec_tmp[line][7]) == 0.0):
            rate = 0.0
        else:
            tmp = float(caseList[line][5]) / float(caseList[line][7])
            rate = "{:.2f}".format(tmp)
        # rec_list[line][0] = rec_tmp[line][2]
        tmp_list.append(caseList[line][2])
        tmp_list.append(caseList[line][3])
        tmp_list.append(rate)
        rec_list.append(tmp_list)
        tmp_list = []

    return render(request, 'server_view/recRate.html',{'data_info':rec_list})

            
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