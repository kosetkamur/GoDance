from rest_framework import serializers
from .models import Course
from ..organizators.serializers import TeacherSerializer
from ..styles.serializers import StyleSerializer


class CourseSerializer(serializers.ModelSerializer):
    style = StyleSerializer(many=False, read_only=True)
    teacher = TeacherSerializer(many=False, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'teacher', 'duration', 'date', 'address', 'count_people', 'shooting',
                  'music', 'age_restrictions', 'style', 'image', 'master_class', 'count_people']
