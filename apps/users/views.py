from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer, UserSerializer
from .permissions import IsSelf

# Create your views here.


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsSelf]
    serializer_class = UserSerializer
    queryset = User.objects.all()


    def get_object(self):
        return self.request.user