from django.shortcuts import render
# import logging
# logger = logging.getLogger(__name__)

from django.http import HttpResponse

from .models import mess, food, order, student

def Home(request):
    messes=mess.objects.all()
    fooditems=food.objects.all()
    return render(request, "Home.html", {"food": fooditems})

def Mess_details(request, mess_id):
    messes=mess.objects.all()
    return render(request, "Mess_details.html", {"Mess": messes})

# Create your views here.
