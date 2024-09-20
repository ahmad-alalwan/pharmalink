from django.db import models
from django.contrib.auth.models import AbstractUser, Group,BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from rest_framework.response import Response    
from rest_framework.decorators import api_view
from rest_framework import status

class PharmacyManager(BaseUserManager):
      def get_queryset(self):
        return super().get_queryset().filter(rank='pharmacy') 
class User(AbstractUser):
    RANK_CHOICES = [
        ('pharmacy', 'Pharmacy'),
        ('DRIVERS', 'Drivers'),
        ('company', 'Company'),
    ]
    id=models.BigAutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    rank = models.CharField(max_length=50, choices=RANK_CHOICES)
    locals=models.TextField()
 
    pharmacy_users = PharmacyManager()
    def __str__(self):
        return self.username      

class DriverManager(BaseUserManager):
      def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(rank='driver')            
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)    
@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        user_rank = instance.rank  # Accessing rank directly from instance

        rank_to_group = {
            'pharmacy': 'group1',
            'DRIVERS': 'Group2',  # Assuming these are the correct mappings
            'company': 'Group3',
        }

        group_name = rank_to_group.get(user_rank)

        if group_name:
            group = Group.objects.get(name=group_name)
            instance.groups.add(group)

