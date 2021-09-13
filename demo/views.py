from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def gallery(request):
    return render(request, 'gallery.html')
