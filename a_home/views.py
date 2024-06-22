from django.shortcuts import render
from .models import *

def home_view(request):
    return render(request, 'home.html')
