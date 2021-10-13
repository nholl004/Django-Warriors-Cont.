from django.shortcuts import render
from django.http import HttpResponse

from .forms import serverForm
from .models import search
# Create your views here.

import csv

caseList = [[]]
infoList = []
line_count = 0
with open('covid_19_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        infoList.append(row[0])
        infoList.append(row[1])
        infoList.append(row[2])
        infoList.append(row[3])
        infoList.append(row[4])
        infoList.append(row[5])
        infoList.append(row[6])
        infoList.append(row[7])
        caseList.append(infoList)
        infoList = []
        #case = {
        #    "SNo": row[0],
        #    "observ":row[1],
        #    "state":row[2],
        #    "country":row[3],
        #    "lastUp":row[4],
        #    "confirm":row[5],
        #    "deaths":row[6],
        #    "recovered":row[7]
        #}
        #caseList.append(case)
        line_count += 1
#print(f'Processed {line_count} lines.')#count = 306430
#print(caseList[1][2])#[1-306429][0-7]


def search(request):
    searched_data = request.POST.get('search')
    print(searched_data)
    x = 0
    
    data_info = [[]]
    print(data_info)
    while( x != line_count-1):
        x += 1
        for y in range(8):
            if(caseList[x][y] == searched_data):
                data_info.append(caseList[x])

    #print(len(data_info))
    if (len(data_info) < 2):
        data_info[0].append("Your search was not found try again...")
        #print(data_info)
    else:
        data_info.pop(0)
        #print(data_info)

    return render(request,'server_view/search.html', {'searched':searched_data,
    'data_info':data_info})

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