from types import NoneType
from django.shortcuts import render
from django.http import HttpResponse

from .forms import serverForm
from .models import search
# Create your views here.

caseList = [[]]
line_count = 0

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

    caseList.append(infoList)
    #print(infoList)
    line_count += 1
caseList.pop(0)
#print(caseList[11347:11349])
def search(request):
    searched_data = request.POST.get('search')
    #print(searched_data)
    x = 0
    data_info = [[]]
    #print(data_info)
    if (searched_data != None):
        while( x != line_count-1):
            x += 1
            for y in range(8):
                if(caseList[x][y] == searched_data):
                    data_info.append(caseList[x])

    #print(len(data_info))
    if (len(data_info)<2 or searched_data > str((len(caseList)))):
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

#This function Deletes the data at the specific SNo value.
#This value is obtained in /search url and requires user input.     
def delete(request):
    delete_index = str(request.POST.get('index'))
    cnt = 0
    data = 0
    #print(delete_index)
    
    #print(caseList[1:5])
    if(delete_index == 'None'):
        return render(request,'server_view/delete.html')
    elif(delete_index != 'None'):
        for i in range(1,len(caseList)-1):
            if(int(caseList[i][0]) == int(delete_index)):
                cnt += 1
                data = caseList[i]
                caseList.pop(i)
        #save result to file
        if(cnt > 0):
            test_file = open("covid_19_data.csv", "w")
            line = ''
            for x in caseList:
                for y in range(0,8):
                    line += x[y]
                    if(y < 7):
                        line += ','
            test_file.write(line)
            test_file.close()
        
        #allows us to delete last value
        elif(int(caseList[len(caseList)-1][0]) == int(delete_index)):
            data = caseList[len(caseList)-1]
            caseList.pop(len(caseList)-1)
            test_file = open("covid_19_data.csv", "w")
            line = ''
            for x in caseList:
                for y in range(0,8):
                    line += x[y]
                    if(y < 7):
                        line += ','
            test_file.write(line)
            test_file.close()
        else:
            data = 'No such index'
        #print(caseList[1:5])
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
        else:
            print('this is where we save file')
            test_file = open("covid_19_data.csv", "w")
            line = ''
            for x in caseList:
                for y in range(0,8):
                    line += x[y]
                    if(y < 7):
                        line += ','
            test_file.write(line)
            test_file.close()
        
        return render(request,'server_view/insert.html',{'error':error,'observ':observ1,'state':state1,'country':country1,
    'lastUp':lastUp1,'confirms':confirms1,'deaths':deaths1,'recovered':recovered1})

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