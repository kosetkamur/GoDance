from rest_framework import serializers
from .models import Organizator, Company, Teacher, TeacherStyle
from ..events.models import Event


from ..courses.models import Course
from ..reviews.models import Review
from ..styles.serializers import StyleSerializer
from ..user.serializers import UserSerializer


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'image', 'rating', 'address']


class TeacherStyleSerializer(serializers.ModelSerializer):
    style = serializers.CharField(source="style.name")
    class Meta:
        model = TeacherStyle
        fields = ["id", "style"]


class TeacherSerializer(serializers.ModelSerializer):
    styles = TeacherStyleSerializer(many=True, read_only=True, source="teacherstyle_set")

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'styles', 'image']




class CourseSerializer(serializers.ModelSerializer):
    style = StyleSerializer(many=False, read_only=True)
    teacher = TeacherSerializer(many=False, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'teacher', 'duration', 'date', 'address', 'count_people', 'shooting',
                  'music', 'age_restrictions', 'style', 'image', 'master_class', 'count_people']



class EventSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'name', 'type', 'description', 'image', 'duration', 'date',
                  'address', 'count_people', 'price', 'present', 'conditions', 'contact', 'teacher']


class OrganizatorReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'author', 'date', 'body', 'rating', 'user']


class OrganizatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizator
        fields = [
            'id',
            "organizator_type",
            'name',
            "schedule",
            "description",
            'image',
            'rating',
            'address',
            "telegram_ref",
            "vk_ref",
            "teachers",
            "courses",
            "master_classes",
            "events",
            "reviews",
        ]

    teachers = TeacherSerializer(many=True)
    courses = CourseSerializer(many=True)
    master_classes = CourseSerializer(many=True)
    events = EventSerializer(many=True)
    reviews = OrganizatorReviewSerializer(many=True)

