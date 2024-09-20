from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login_view/',views.login_view,name='login'),
    path('api_token',obtain_auth_token),
    path('sing/',views.sinup),
  
]   