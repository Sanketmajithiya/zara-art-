from django.urls import path
from .views import *

urlpatterns = [
   path('', ticketList, name='ticketList')
]