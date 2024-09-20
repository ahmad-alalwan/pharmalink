from django.db import models
from datetime import*
from account.models import *

class Pharmacy(models.Model):
    pharmacy=PharmacyManager()
    
'''class Pharmacy(models.Model):
    name=models.CharField(max_length=25)
    account=models.ForeignKey(User,on_delete=models.CASCADE)
    id=models.BigAutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    locals=models.TextField()   
    def __str__(self):
        return self.name'''
class Medicine(models.Model):
    name=models.CharField(max_length=20,unique=True,blank=True)
    id_pharmacy=models.ForeignKey(Pharmacy,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.CharField(max_length=50)
    date=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name    
class Orders(models.Model):
    pharmacy=models.OneToOneField(Pharmacy,on_delete=models.CASCADE)
    account=models.IntegerField()
    invoice=models.IntegerField(primary_key=True)
    
class Register_medicien(models.Model):
    name_pharmacy=models.ForeignKey(Pharmacy,on_delete=models.CASCADE)
    id=models.BigAutoField(primary_key=True)
    name_medicine=models.CharField(max_length=50)
    quantity=models.IntegerField()
    date=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return str(self.name_pharmacy)

class Size_order(models.Model):
    quantity=models.IntegerField()
    id_name_medicien=models.OneToOneField(Medicine,on_delete=models.CASCADE)
    id_pharmacy=models.ForeignKey(Pharmacy,on_delete=models.CASCADE)
    

             
    
    

    


    