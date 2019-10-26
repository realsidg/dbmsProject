from django.db import models

class student(models.Model):
    Student_id = models.CharField(max_length=100, primary_key=True)
    Name = models.CharField(max_length=100)
    Mess_id = models.ForeignKey('mess', on_delete=models.PROTECT)
    Password = models.CharField(max_length=100)
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

# InBuilt with Django
# class admin(models.Model):
#     Admin_id = models.CharField(max_length=20, primary_key=True)
#     Username = models.CharField(max_length=20)
#     Password = models.CharField(max_length=20)

class food(models.Model):
    Food_id= models.CharField(max_length=20, primary_key=True)
    Name= models.CharField(max_length=20)
    Cost= models.CharField(max_length=20)

    def __str__(self):
        return self.Name

class order(models.Model):
    Order_id= models.CharField(max_length=20, primary_key=True)
    Food_id= models.ForeignKey("food", on_delete=models.PROTECT)
    Time= models.DateField()

    def __str__(self):
        return self.Order_id
