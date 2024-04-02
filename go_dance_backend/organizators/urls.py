from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizatorViewSet, TeacherViewSet

router = DefaultRouter()
router.register(r'organizator', OrganizatorViewSet, basename='organizator')
router.register(r'teacher', TeacherViewSet, basename='teacher')

urlpatterns = [
    path('', include(router.urls)),
]