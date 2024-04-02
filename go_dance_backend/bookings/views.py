from django.db import transaction
from rest_framework import views, filters, status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from go_dance_backend.bookings.models import Seance
from go_dance_backend.bookings.serializers import SeanceSerializer, BookingSerializer, CourseBookingSerializer


class SeanceDateFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        queryset = queryset.filter(is_free=True)
        if request.query_params.get("date") and request.query_params.get("teacher"):
            return queryset.filter(
                time__date=request.query_params["date"],
                teacher_id=request.query_params["teacher"],
            )
        return queryset


class GetSeancesList(ListAPIView):
    queryset = Seance.objects.all()
    serializer_class = SeanceSerializer
    filter_backends = [SeanceDateFilterBackend]
    filterset_fields = ['date', 'teacher']


class CreateBookingView(CreateAPIView):
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            data = request.data
            data["user_id"] = request.user.id
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            Seance.objects.filter(id=serializer.data["seance_id"]).update(is_free=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CreateCourseBookingView(CreateAPIView):
    serializer_class = CourseBookingSerializer

    def create(self, request, *args, **kwargs):
        data = dict(request.data)
        data["user_id"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)