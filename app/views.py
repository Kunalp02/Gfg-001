from django.shortcuts import render, HttpResponse
from . models import User
from django.db.models import Q


def show_all(request):
    users = User.objects.all() # This command outputs all user objects that we have created at start.
    return render(request, 'show_details.html' , context={'users':users})


def show_indians(request):
    # 1st solution
    show_indians = User.objects.filter(country='India').exclude(country='Japan') 
    return render(request, 'show_details.html' , context={'show_indians':show_indians})


def show_non_indians(request):
    # 2nd Solution
    show_non_indians = User.objects.filter(~Q(country='India'))  
    return render(request, 'show_details.html' , context={'show_non_indians':show_non_indians})



