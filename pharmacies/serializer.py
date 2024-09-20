from rest_framework import serializers
from .models import *

class Pharmacy_serializer(serializers.ModelSerializer):
    class Meta:
        model=Pharmacy
        fields='__all__' 
class Medicine_sale_serializer(serializers.ModelSerializer):
    class Meta:
        model=Medicine
        fields=('name','quantity')

class Medicine_serializer(serializers.ModelSerializer):
    class Meta:
        model=Medicine
        fields=('name','quantity','price','id_pharmacy')

class Register_Medicien_serializer(serializers.ModelSerializer):
    class Meta:
        model=Register_medicien
        fields='__all__'           
class Register_pharmacy_serializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields=('name_pharmacy','name_medicine','quantity')
    
class All_data(serializers.ModelSerializer):
    class Meta:
        forkey1 = serializers.SlugRelatedField(many=False, slug_field='medicine', queryset=Medicine.objects.all())
        forkey2 = serializers.SlugRelatedField(many=False, slug_field='register', queryset=Register_medicien.objects.all())
        model=Pharmacy
        fields=('name','locals','forkey1','forkey2')
class Order_serializer(serializers.ModelSerializer):
    class Meta:
        #forkey1 = serializers.SlugRelatedField(many=False, slug_field='medicine', queryset=Medicine.objects.all())
        model=Size_order
        fields='__all__' 

class Add_medicien(serializers.ModelSerializer):
    class Meta:
        forkey = serializers.SlugRelatedField(many=False, slug_field='medicine', queryset=Medicine.objects.all())
        models = Size_order 
        fields=('id_name_medicien','quantity','forkey')


