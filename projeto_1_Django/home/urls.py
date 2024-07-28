from django.urls import path
from . import views

app_name = 'homepage' # Namespace do url da Home

urlpatterns = [
    path('', views.home, name= 'home_index') # Id name
]