from django.shortcuts import render

def index(request):
    return render(request, 'pictures_app/index.html')


