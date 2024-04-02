from rest_framework import serializers
from .models import Seance, Booking, UserCourseBooking


class SeanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seance
        fields = ['id', 'time', "teacher_id", "is_free"]


class BookingSerializer(serializers.Serializer):
    seance_id = serializers.IntegerField(required=True)
    user_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Booking.objects.create(**validated_data)


class CourseBookingSerializer(serializers.Serializer):
    course_id = serializers.IntegerField(required=False)
    user_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return UserCourseBooking.objects.create(**validated_data)