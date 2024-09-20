from django.urls import path,include
from . import views

urlpatterns = [
    path('add_pharmacy/',views.add_pharmacies),
    path('export_allpharmacy_pdf/',views.export_pdf),
    path('all_pharmcies/',views.all_Pharmcies),
    path('unactive/',views.unactive_pharamcy),
    path('delet_ph/',views.delete_pharmacy),
    path('count_ph/',views.counter_pha),
]