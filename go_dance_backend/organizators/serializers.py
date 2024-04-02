from rest_framework import serializers
from .models import Organizator, Company, Teacher, TeacherStyle

class OrganizatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizator
        fields = ['id', 'name', 'image', 'rating', 'address']

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
        fields = ['id', 'name', 'styles']
