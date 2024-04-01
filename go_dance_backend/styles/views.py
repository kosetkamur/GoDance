from rest_framework import viewsets
from .models import Style
from .serializers import StyleSerializer

class StyleViewSet(viewsets.ModelViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer