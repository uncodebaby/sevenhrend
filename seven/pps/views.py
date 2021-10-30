from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def roompage(request):
    return render(request, 'room.html')