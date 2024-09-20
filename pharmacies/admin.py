from django.contrib import admin
from .models import *
from guardian.admin import GuardedModelAdmin
from account.models import User 
from guardian.shortcuts import get_objects_for_user

class Show2(admin.ModelAdmin):
    list_display=[ 'name','quantity','price']   
admin.site.register(Pharmacy)
admin.site.register(Medicine,Show2)
admin.site.register(Orders)
admin.site.register(Register_medicien)
admin.site.register(Size_order)


   
      
