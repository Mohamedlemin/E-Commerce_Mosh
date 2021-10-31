from django.http.response import HttpResponse
from django.shortcuts import render


def say_hello(request):
    x = 1
    x = 2
    return render(request, 'hello.html', {'name': 'Mohamed Lemin'})
