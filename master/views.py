from django.shortcuts import render
from .serializers import TicketSerializers
from .models import Ticket
from rest_framework.decorators import api_view # https://www.django-rest-framework.org/api-guide/views/
from rest_framework.response import Response # https://www.django-rest-framework.org/tutorial/3-class-based-views/
from rest_framework import status

@api_view(['GET', 'POST'])
def ticketList(request):
    # add new data
    if request.method == 'POST':
        serializer = TicketSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # get all data
    if request.method == 'GET':
        querySet = Ticket.objects.all()
        serializer = TicketSerializers(querySet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





# get specific data
# update specific all data
# update specific data
# delete specific data