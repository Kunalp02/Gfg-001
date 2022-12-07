from django.shortcuts import render, HttpResponse
from . models import User
from django.db.models import Q
# Create your views here.

def get_info(request):
    users = User.objects.all() # This command outputs all user objects that we have created at start.
    print(users)

    # 1st solution
    users = User.objects.filter(country='India').exclude(country='Japan')
    for user in users:
        print("Persons belongs to India", user.user_name)

    # 2nd Solution
    users = User.objects.filter(~Q(country='India'))  

    for user in users:
        print("Persons belongs to Japan", user.user_name)

    return HttpResponse('Done!')

