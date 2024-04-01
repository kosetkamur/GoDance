from rest_framework import viewsets
from .models import Organizator
from .serializers import OrganizatorSerializer
from django_filters.rest_framework import DjangoFilterBackend

class OrganizatorViewSet(viewsets.ModelViewSet):
    model = Organizator
    filter_backends = [DjangoFilterBackend]
    queryset = Organizator.objects.all()
    serializer_class = OrganizatorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['teacher__teacher_styles__style_id']