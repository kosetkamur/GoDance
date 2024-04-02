from django.urls import path

from go_dance_backend.bookings.views import GetSeancesList, CreateBookingView, CreateCourseBookingView

urlpatterns = [
    path("seance", CreateBookingView.as_view()),
    path("course", CreateCourseBookingView.as_view()),
    path('seances', GetSeancesList.as_view()),
]