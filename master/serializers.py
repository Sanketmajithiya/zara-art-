from rest_framework import serializers
from .models import Ticket

class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        # fields = ['title', 'content']
        fields = '__all__'