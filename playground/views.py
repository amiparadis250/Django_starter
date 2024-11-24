from django.shortcuts import render
from django.http import HttpResponse

# Example of a function-based view
def hello(request):
    return render(request, 'index.html')


def Login(request):
    return render(request, 'login.html')