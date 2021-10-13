from django.shortcuts import render
from django.http import HttpResponse

from .forms import serverForm
from .models import search
# Create your views here.
def search(request):
    searched_data = request.POST.get('search')
    print(searched_data)
    return render(request,'server_view/search.html', {'search':searched_data})

def searched(request):
    queryset = search.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "server_view/search_list.html", context)


def searching(request):
    search_form = serverForm()
    if request.method == "POST":
        search_form = serverForm(request.POST)
        if search_form.is_valid():
            #print(search_form.cleaned_data)
            search.objects.create(**search_form.cleaned_data)
        else:
            print(search_form.errors)
    context = {
        'form': search_form,
    }
    return render(request, "server_view/create_view.html", context)

def test(request,*args, **kwargs):
    return HttpResponse('Hello World')

def test1(request, *args, **kwargs):
    return render(request, 'test.html', {})