from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Hello World! You're at the polls index.")