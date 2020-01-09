from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello World,\nMy Name is Justice Ntia, \n\n\nThis is was my first Django web hosting/server bla bla bla.\nThank You")


