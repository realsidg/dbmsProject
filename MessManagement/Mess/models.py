from django.db import models
from django.contrib.auth.models import User

class student(models.Model):
    Student_id = models.CharField(max_length=100, primary_key=True)
    Name = models.CharField(max_length=100)
    Mess_id = models.ForeignKey('mess', on_delete=models.PROTECT)
    Password = models.CharField(max_length=256)
    Balance = models.FloatField(max_length=100)

    def __str__(self):
        return self.Name

class mess(models.Model):
    blocks=[(chr(i),chr(i)) for i in range(65,82)]
    Mess_id = models.CharField(max_length=50, primary_key=True)
    Block = models.CharField(choices=blocks, max_length=1)
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
=
class food(models.Model):
    Food_id= models.CharField(max_length=20, primary_key=True)
    Name= models.CharField(max_length=20)
    Cost= models.CharField(max_length=20)

    def __str__(self):
        return self.Name

class order(models.Model):
    id = models.AutoField(primary_key=True)
    Time= models.DateField()
    Student_id= models.ForeignKey("student", on_delete=models.PROTECT)
    Mess_id = models.ForeignKey("mess", on_delete=models.PROTECT)


class cart(models.Model):
    Food_id= models.ForeignKey("food", on_delete=models.PROTECT)
    Order_id= models.ForeignKey("order", on_delete=models.PROTECT)
    quantity= models.IntegerField()
    def __str__(self):
        return str(self.Order_id)