from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def models_list(request):
    random_number = random.randint(1, 100)
    return HttpResponse (f"Random number: {random_number}")