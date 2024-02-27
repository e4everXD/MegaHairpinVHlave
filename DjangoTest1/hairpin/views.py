from django.shortcuts import render
from django.shortcuts import HttpResponse
import random

def models_list(request):
    random_number = random.randint(0, 1000)
    return render(request, 'hairpin/random.html', {'random': random_number})