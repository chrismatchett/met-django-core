from django.shortcuts import render

# Create your views here.

def react_home(request):
    return render(request, 'react/main.html')
