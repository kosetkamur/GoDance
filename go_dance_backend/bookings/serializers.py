from rest_framework import serializers
from .models import Course, Teacher, Style
from ..organizators.serializers import TeacherSerializer


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'name', 'style', 'date', 'description', 'image', 'duration', 'address', 'count_people', 'price', 'music', 'shooting', 'age_restrictions', 'teacher']
