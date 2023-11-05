from django.shortcuts import render
import random

def index(request):
    random_number = random.randint(1, 10000)
    context = {'random_number': random_number}
    return render(request, 'index2.html', context)
