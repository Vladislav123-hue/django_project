from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("About section")
