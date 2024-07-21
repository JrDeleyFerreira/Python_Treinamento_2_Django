from django.urls import path
from . import views

urlpatterns = [
    path('', view= views.blog),
    path('authors/', view= views.authors),
]

