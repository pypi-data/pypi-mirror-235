from django.utils.timezone import datetime
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = Ticket
        fields = ['email', 'subject', 'text', 'meta']

    def validate_email(self, value):
        if self.Meta.model.objects.filter(email=value, created__date=datetime.today()).count() >= 3:
            raise ValidationError("You have sent in the maximum amount of tickets. Please try again later.")
        return value
