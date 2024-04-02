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


class UserCurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'birthdate', 'phone', 'email', 'master_classes', 'course_bookings']

    master_classes = BookingSerializer(many=True, read_only=True)
    course_bookings = UserCourseBookingSerializer(many=True, read_only=True)


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
