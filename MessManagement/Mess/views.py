from django.shortcuts import render
# import logging
# logger = logging.getLogger(__name__)

from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


from .models import mess, food, order, student, User
from .forms import SignInForm

# url = reverse('Home')

def login(request):
    message=""
    if request.method == 'POST':
        form = SignInForm(request.POST)
        foodi=food.objects.all()
        # print(request.POST)
        if form.is_valid():
            stud=student.objects.filter(Student_id=request.POST['user_regno'])[0]
            if stud.Password == request.POST['user_pass']:
                return render(request, "index.html",{'student':stud,'food':foodi})
            else:
                message="Invalid Credentials"

    else:
        form = SignInForm()
    
    return render(request, "login.html", {"form":form,'message':message})

def home(request):
    try:
        query=request.GET['q']
    except:
        query=''
    if query=='':
        foodi=food.objects.all()
    else:
        foodi=food.objects.filter(Food_id__contains=query)|food.objects.filter(Name__contains=query)
    stud=student.objects.filter(Student_id=request.GET['sid'])[0]
    return render(request, "index.html",{'student':stud,'food':foodi})

def orders(request):
    return HttpResponse([i for i in request.GET])

def Mess_details(request, mess_id):
    messes=mess.objects.all()
    return render(request, "Mess_details.html", {"Mess": messes})

# Create your views here.
