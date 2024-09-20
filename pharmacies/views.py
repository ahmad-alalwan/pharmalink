from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view 
from rest_framework import status
from rest_framework.response import Response
from django.http import FileResponse
from reportlab.lib import colors
from django.http.response import JsonResponse
from .models import *
from .serializer import *
from django.db.models import Avg,Sum,Count
from django.shortcuts import get_object_or_404
from django.views import View
import csv
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import LETTER
import io

@api_view(['GET'])
def search_mdicine(request,pk):
    item=Medicine.objects.get(name=pk)
    if request.method == 'GET':
        serializer=Medicine_serializer(item) 
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['PUT'])
def sale(request,pk,number):
    item=Medicine.objects.get(name=pk)
    if request.method=='PUT':
        quantity_old=item.quantity
        quantity_new=quantity_old-number
        item.quantity = quantity_new
        item.save()        
        serializer=Medicine_serializer(item)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def search_pharmacy(request,pk):
    item=Pharmcay.objects.get(name=pk)
    if request.method == 'GET':
        serializer=Pharmacy_serializer(item) 
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def details_pharmacy(request,pk):
    if request.method == 'GET':
        pharmacy = get_object_or_404(Pharmacy, id=pk)
        medicines = Medicine.objects.filter(id_pharmacy=pharmacy.id)
        register = get_object_or_404(Register, pharmacy=pharmacy)
        pharmacy_serializer = Pharmacy_serializer(pharmacy)
        medicine_serializer =Medicine_serializer(medicines, many=True)
        register_serializer = Register_serializer(register)
        response_data = {
            'pharmacy': pharmacy_serializer.data,
            'medicines': medicine_serializer.data,
            'register': register_serializer.data,
        }    
        return Response(response_data,status=status.HTTP_200_OK)

@api_view(['POST'])                                                                                   
def add_medicien(request): 
    if request.method =='POST':
        seralizer=Add_medicien(data=request.data)
        if seralizer.is_valid():
           seralizer.save()
           return Response(seralizer.data,status=status.HTTP_200_OK)

@api_view(['GET']) 
def export_pdf(request):
    buf=io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=LETTER)
    styles = getSampleStyleSheet()
    pharmacies = Pharmacy.objects.all()
    list=[]
    data=[['Pharmacy Name', 'Location']]
    for item in pharmacies:
        data.append([item.name, item.locals])
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    list.append(table)
    doc.build(list) 
    buf.seek(0)
    return FileResponse(buf,as_attachment=True,filename="name.pdf")
    
@api_view(['GET'])
def all_medicine(request,pk):
    try:
        item = Medicine.objects.get(id_pharmacy=pk)
        serializer = Medicine_serializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Medicine.DoesNotExist:
        return Response({"detail": "Medicine not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def Orders(request):
        if request.method == 'POST':
           serializer = Order_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # 201 is more appropriate for creation
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


