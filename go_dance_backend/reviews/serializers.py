from rest_framework import serializers
from .models import Review
from ..organizators.serializers import OrganizatorSerializer
from ..user.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    organizator = OrganizatorSerializer(many=False, read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'author', 'date', 'body', 'rating', 'organizator', 'user']
