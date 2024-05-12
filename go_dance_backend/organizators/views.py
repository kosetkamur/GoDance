from django.db.models import Q
from rest_framework import viewsets, filters
from .models import Organizator, Teacher



class OrganizatorStyleFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        if request.query_params.get("style_id"):
            return queryset.filter(
                Q(teacher__teacherstyle__style_id=request.query_params["style_id"]) |
                Q(company__companystyle__style_id=request.query_params["style_id"])
            )
        return queryset


class OrganizatorViewSet(viewsets.ModelViewSet):
    from .serializers import OrganizatorSerializer
    model = Organizator
    queryset = Organizator.objects.all().select_related('company', 'teacher')
    serializer_class = OrganizatorSerializer
    filter_backends = [OrganizatorStyleFilterBackend]
    filterset_fields = ['style_id']


class TeacherViewSet(viewsets.ModelViewSet):
    from .serializers import TeacherSerializer
    model = Teacher
    queryset = Teacher.objects.all().prefetch_related("teacherstyle_set")
    serializer_class = TeacherSerializer
