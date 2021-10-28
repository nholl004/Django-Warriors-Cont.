from types import NoneType
from django.shortcuts import render
from django.http import HttpResponse

from .forms import serverForm
from .models import search
# Create your views here.

caseList = [[]]
line_count = 0
import_cnt = 0
def importButton(request):
    global import_cnt
    if(import_cnt == 0):
    # print(request.POST.get('filename'))
        importFunction()
        import_cnt += 1

    return render(request, 'server_view/import.html')

def importFunction():
    csv_file = open("covid_19_data.csv")
    global line_count 
    global caseList
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

        caseList.append(infoList)
        # print(infoList)
        line_count += 1
    caseList.pop(0)
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
    list = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

    for i in range(1,len(tmp)):
        if(float(list[0][5])<float(tmp[i][5]) and float(list[0][5])<=float(list[1][5]) and float(list[0][5])<=float(list[2][5])):
            list.pop(0)
            list.append(tmp[i])
        elif(float(list[1][5])<float(tmp[i][5]) and float(list[1][5])<=float(list[0][5]) and float(list[1][5])<=float(list[2][5])):
            list.pop(1)
            list.append(tmp[i])
        elif(float(list[2][5])<float(tmp[i][5]) and float(list[2][5])<=float(list[0][5]) and float(list[2][5])<=float(list[1][5])):    
            list.pop(2)
            list.append(tmp[i])

    print(list)
    return render(request, 'server_view/top_cases.html',{'data_info':list})    

def top_deaths(request):
    global caseList
    tmp = caseList
    list = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

    for i in range(1,len(tmp)):
        if(float(list[0][6])<float(tmp[i][6]) and float(list[0][6])<=float(list[1][6]) and float(list[0][6])<=float(list[2][6])):
            list.pop(0)
            list.append(tmp[i])
        elif(float(list[1][6])<float(tmp[i][6]) and float(list[1][6])<=float(list[0][6]) and float(list[1][6])<=float(list[2][6])):
            list.pop(1)
            list.append(tmp[i])
        elif(float(list[2][6])<float(tmp[i][6]) and float(list[2][6])<=float(list[0][6]) and float(list[2][6])<=float(list[1][6])):    
            list.pop(2)
            list.append(tmp[i])

    print(list)
    return render(request, 'server_view/top_deaths.html',{'data_info':list})    


def top_recov(request):
    global caseList
    tmp = caseList
    list = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

    for i in range(1,len(tmp)):
        #tmp[i][7] = tmp[i][7][0:len(tmp[i][7])-1]
        #print(tmp[i][7])
        if(float(list[0][7])<float(tmp[i][7]) and float(list[0][7])<=float(list[1][7]) and float(list[0][7])<=float(list[2][7])):
            list.pop(0)
            list.append(tmp[i])
        elif(float(list[1][7])<float(tmp[i][7]) and float(list[1][7])<=float(list[0][7]) and float(list[1][7])<=float(list[2][7])):
            list.pop(1)
            list.append(tmp[i])
        elif(float(list[2][7])<float(tmp[i][7]) and float(list[2][7])<=float(list[0][7]) and float(list[2][7])<=float(list[1][7])):    
            list.pop(2)
            list.append(tmp[i])

    print(list)
    return render(request, 'server_view/top_recov.html',{'data_info':list})    


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
    serialNo = str(request.POST.get('index'))
    context = {}
    if not serialNo:
        error = True
        return render(request,'server_view/confirmtodeath.html',{'error':error,'index':serialNo })
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
                return render(request,'server_view/confirmtodeath.html',context, {'error':error,'index':serialNo})
            else:
                error = True;    

    return render(request,'server_view/confirmtodeath.html',{'error':error,'index':serialNo })
      
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


            
# def searched(request):
#     queryset = search.objects.all()
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "server_view/search_list.html", context)


# def searching(request):
#     search_form = serverForm()
#     if request.method == "POST":
#         search_form = serverForm(request.POST)
#         if search_form.is_valid():
#             #print(search_form.cleaned_data)
#             search.objects.create(**search_form.cleaned_data)
#         else:
#             print(search_form.errors)
#     context = {
#         'form': search_form,
#     }
#     return render(request, "server_view/create_view.html", context)

# def test(request,*args, **kwargs):
#     return HttpResponse('Hello World')

# def test1(request, *args, **kwargs):
#     return render(request, 'test.html', {})
