from django.urls import path
from .views import CurrentUserView, UserRegistration, UserLogin

urlpatterns = [
    path('user_current/', CurrentUserView.as_view()),
    path('registration/', UserRegistration.as_view()),
    path('login/', UserLogin.as_view()),
]