from rest_framework import serializers

from go_dance_backend.bookings.models import Booking, UserCourseBooking
from go_dance_backend.user.models import User


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id', 'duration', 'time'
        ]


class UserCourseBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourseBooking
        fields = [
            'id', 'name', 'style', 'duration', 'is_confirmed'
        ]


class SimpleOrganizatorSerializer(serializers.Serializer):
    teacher_id = serializers.IntegerField(allow_null=True)
    company_id = serializers.IntegerField(allow_null=True)

class UserCurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'birthdate', 'phone', 'email', 'master_classes', 'course_bookings', 'organizator_info']

    master_classes = BookingSerializer(many=True, read_only=True)
    course_bookings = UserCourseBookingSerializer(many=True, read_only=True)
    organizator_info = SimpleOrganizatorSerializer(read_only=True, source="organizator")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'birthdate', 'phone', 'email']




class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name', 'birthdate', 'phone', 'email', 'password', 'photo'
        ]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
