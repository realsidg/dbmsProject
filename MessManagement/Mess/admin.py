from django.contrib import admin

from .models import mess, student, food, order

@admin.register(mess)
class messAdmin(admin.ModelAdmin):
    pass
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    pass
@admin.register(food)
class foodAdmin(admin.ModelAdmin):
    pass
@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    pass
# Register your models here.
