from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class CurrentUserView(APIView):
    def get(self, request):
        user_id = request.user.id
        try:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=400, data={'error': 'User not found'})