from rest_framework import serializers
from .models import Event
from ..organizators.serializers import TeacherSerializer


class EventSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'name', 'type', 'description', 'image', 'duration', 'date',
                  'address', 'count_people', 'price', 'present', 'conditions', 'contact', 'teacher']