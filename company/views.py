from django.shortcuts import render
from pharmacies.models import *
from pharmacies.serializer import *
from rest_framework.decorators import api_view 
from rest_framework import status
from rest_framework.response import Response
from account.models import *

@api_view(['POST'])
def add_pharmacies(request):
    serializer=Pharmacy_serializer(data=request.data)
    if serializer.is_valid:
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['GET'])   
def counter_pha(request):
    item= Pharmacy.objects.all().count()
    return Response({"count": item},status=status.HTTP_200_OK)

@api_view(['GET'])
def all_Pharmcies(request):
    item=Pharamcy.objects.all()
    serializer=Pharmacy_serializer(item)
    return Response(seralizer.data,status=status.HTTP_200_OK)

@api_view(['PUT'])
def unactive_pharamcy(request):
    try:
        # Retrieve the pharmacy by name from the request data
        name = request.data.get('name')
        item = Pharmacy.objects.get(name=name)
        
        # Update the is_active field
        item.is_active = False  # Corrected the typo here
        item.save()

        # Serialize the updated pharmacy object
        serializer = Pharmacy_serializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Pharmacy.DoesNotExist:
        # Handle the case where the pharmacy does not exist
        return Response({'error': 'Pharmacy not found.'}, status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def delete_pharmacy(request):
    item=Pharmacy.objects.get(name=request.data)
    if request.method =='DELETE':
        item.delete()
        serializer=Pharmacy_serializer(item)
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


