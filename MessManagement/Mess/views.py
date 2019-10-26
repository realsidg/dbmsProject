from django.shortcuts import render
# import logging
# logger = logging.getLogger(__name__)

from django.http import HttpResponse

from .models import mess

def Home(request):
    messes=mess.objects.all()
    return render(request, "Home.html", {"Mess": messes})

def Mess_details(request, mess_id):
    messes=mess.objects.all()
    return render(request, "Mess_details.html", {"Mess": messes})

# Create your views here.
