from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreateDemand.as_view(), name='list_create_demand')
]
