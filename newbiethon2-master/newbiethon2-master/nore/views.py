from django.shortcuts import render, get_object_or_404, redirect
from .forms import RoomForm
from .models import Room

# Create your views here.

def search_map(request):
    if request.method=='POST':
        norebang = request.POST['norebang']
        rooms = Room.objects.filter(norebang=norebang)
        return render(request, 'list.html', {'rooms': rooms})
    else:
        return redirect('main')

def list(request):
    if request.method=='POST':
        norebang = request.POST['norebang']
        rooms = Room.objects.filter(norebang='norebang')
        return render(request, 'list.html', {'rooms': rooms})
    else:
        return redirect('main')

def show(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'show.html', {'room': room})

def new(request):
    return render(request, 'new.html')

def noreroom_1(request):
    return render(request, 'noreroom_1.html')

def noreroom_2(request):
    return render(request, 'noreroom_2.html')

def noreroom_3(request):
    return render(request, 'noreroom_3.html')

def noreroom_4(request):
    return render(request, 'noreroom_4.html')

def roomcreate(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.user = request.user
            room.save()
            return redirect('list')
    else:
        form = RoomForm()
        return render(request, 'new.html', {'form': form})