from django.db.models import Q
from rest_framework import viewsets, filters
from .models import Event
from .serializers import EventSerializer


class EventStyleFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        if request.query_params.get("style_id"):
            return queryset.filter(
                Q(teacher__teacherstyle__style_id=request.query_params["style_id"]) |
                Q(organizatorevent__organizator__company__companystyle__style_id=request.query_params["style_id"])
            )
        return queryset


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [EventStyleFilterBackend]
    filterset_fields = ['style_id']
