from django.urls import path,include
from . import views


urlpatterns = [
    path('search/<str:pk>',views.search_mdicine,name='search'),
    path('sale/<str:pk>/<int:number>',views.sale),
    path('search_pharmacy/<str:pk>',views.search_pharmacy,name='search_pharmacy'),
    path('details_pharmacy/<str:pk>',views.details_pharmacy),
    path('add_medicien/',views.add_medicien),
   # path('add_pharmacies/',views.add_pharmacies),
    path('export_pdf/',views.export_pdf),
    path('medicines/<int:pk>',views.all_medicine),
    path('order/',views.Orders),

]