from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizatorViewSet

router = DefaultRouter()
router.register(r'organizator', OrganizatorViewSet, basename='organizator')

urlpatterns = [
    path('', include(router.urls)),
]