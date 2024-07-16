from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    msg="This is homepage"
    return HttpResponse(msg)