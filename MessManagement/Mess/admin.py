from django.contrib import admin

from .models import mess, student, food, order, cart

@admin.register(mess)
class messAdmin(admin.ModelAdmin):
    list_display=['Name', 'Block']
    pass
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    pass
@admin.register(food)
class foodAdmin(admin.ModelAdmin):
    pass
@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    list_display=['id', 'Student_id','Mess_id']
    pass

@admin.register(cart)
class messAdmin(admin.ModelAdmin):
    list_display=['Order_id', 'Food_id','quantity']
    pass
# Register your models here.
