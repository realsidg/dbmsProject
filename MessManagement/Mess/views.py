from django.shortcuts import render
# import logging
# logger = logging.getLogger(__name__)

from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.db import connection


from .models import mess, food, order, student, User, cart
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
    cart1=[]
    fq=[]
    total=0
    print(request.GET.items)
    for i,j in list(request.GET.items()):
        if i!="sid":
            if int(j)>0:
                f= (food.objects.filter(Food_id=i)[0])
                total+=int(f.Cost)*int(j)
                quan=int(j)
                tot=int(f.Cost)*int(j)
                fi=f.Food_id
                cart1.append(f)
                fq.append([quan,fi])
    stud=student.objects.filter(Student_id=request.GET['sid'])[0]
    Student_id = student.objects.only('Student_id').get(Student_id=stud.Student_id)
    ords= order(Time=datetime.now(), Student_id=Student_id, Mess_id=stud.Mess_id)
    ords.save()
    # ords.save()
    # with connection.cursor() as cursor:
    #     cursor.execute("INSERT INTO order values (Time=%s, Student_id=%s, Mess_id=%s);",[datetime.now(), stud.Student_id, str(stud.Mess_id)] )
    #     row = cursor.fetchone()

    for i,j in fq:
        if(i>0):
            Food_id = food.objects.only('Food_id').get(Food_id=j)
            Order_id = order.objects.only('id').get(id=ords.id)
            crt_item= cart(Order_id=Order_id, Food_id=Food_id, quantity=i) 
            crt_item.save()
    stud.Balance= stud.Balance - total
    stud.save()
    return render(request, 'Cart.html', {"cart":cart1,"total":total,'qt':fq,'student':stud,'ordid':ords.id})


# Create your views here.
