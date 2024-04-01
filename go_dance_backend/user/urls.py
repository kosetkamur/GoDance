from django.urls import path
from .views import CurrentUserView

urlpatterns = [
    path('user_current/', CurrentUserView.as_view()),
]