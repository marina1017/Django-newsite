from django.contrib import admin
from .models import Message_bord
# Register your models here.

class Message_bordAdmin(admin.ModelAdmin):
    list_display = ('id','new_message')
    
admin.site.register(Message_bord,Message_bordAdmin)
