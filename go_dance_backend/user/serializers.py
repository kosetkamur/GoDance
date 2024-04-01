from rest_framework import serializers

from go_dance_backend.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'birthdate', 'phone', 'email']
