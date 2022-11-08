from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def candidate(request):
    return render(request, 'candidate.html')