from django.contrib.auth import login, authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, UserRegistrationSerializer, UserLoginSerializer, UserCurrentSerializer, \
    BookingSerializer, UserCourseBookingSerializer
from ..bookings.models import UserCourseBooking, Booking


class CurrentUserView(APIView):
    def get(self, request):
        user_id = request.user.id
        try:
            user = User.objects.get(id=user_id)
            user.master_classes = Booking.objects.filter(user_id=user_id)
            user.course_bookings = UserCourseBooking.objects.filter(user_id=user_id)
            serializer = UserCurrentSerializer(
                instance=user,
            )
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=400, data={'error': 'User not found'})


class UserRegistration(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        login(request, serializer.instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserLogin(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)
        serializer = UserLoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
