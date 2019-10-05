from django.shortcuts import render, redirect
from .forms import SearchForm
from nore.models import Room

# Create your views here.
def search(request):
    form = SearchForm()
    return render(request, 'search.html', {'form': form})

def result(request):
    title = ''
    genre = ''
    ages = ''
    if request.GET['title']:
        title = request.GET['title']
    if request.GET['genre']:
        genre = request.GET['genre']
    if request.GET['ages']:
        ages = request.GET['ages']
    rooms = Room.objects.all
    if request.GET['title']:
        rooms = Room.objects.filter(title=title)
    if request.GET['genre']:
        rooms = Room.objects.filter(genre=genre)
    if request.GET['ages']:
        rooms = Room.objects.filter(ages=ages)
    # rooms = Room.objects.filter(title=title, genre=genre, ages=ages)

    return render(request, 'result.html', {'rooms': rooms, 'title': title, 'genre': genre, 'ages': ages})

# def search_map(request):
#     if request.method=='POST':
#         norebang = request.POST['norebang']
#         rooms = Room.objects.filter(norebang='norebang')
#         return render(request, 'result_map.html', {'rooms': rooms})
#     else:
#         return redirect('main')

def result_map(request):
    return render(request, views.result_map)