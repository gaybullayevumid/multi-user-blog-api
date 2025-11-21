from rest_framework import generics, permissions
from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer, UserSerializer

# Create your views here.


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_object(self):
        return self.request.user
