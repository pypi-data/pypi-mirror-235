import re
import json

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .serializers import TicketSerializer
from .models import Ticket


class TicketCreateAPIView(CreateAPIView):
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        if self.request.user.is_authenticated:
            instance.user = self.request.user
            instance.save(update_fields=['user'])


class TicketMetaRetrieveView(RetrieveAPIView):
    serializer_class = TicketSerializer
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        ticket = get_object_or_404(Ticket, id=kwargs.get('pk'))
        response = HttpResponse(json.dumps(ticket.meta, indent=4), content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename={}.json'.format(re.sub(r'\s+', '_', ticket.subject))
        return response
