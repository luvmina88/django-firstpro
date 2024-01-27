from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'second.html')
