from django.shortcuts import render

def index(request):
    data = {
        'title': 'main list11',
        'values': ['some', 'hello', 'hahaha'],
        'obj': {
            'car': 'bmw',
            'age': 18,
            'hobby': 'biser'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
