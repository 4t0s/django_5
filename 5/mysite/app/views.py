from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request): 
    return HttpResponse(""" <h1>This is the home page</h1> """)

def retrieve(request, id):
    return HttpResponse(f""" <h1>This is {id} retrieve page</h1>""")
