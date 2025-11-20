from rest_framework import generics
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model

# Create your views here.


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

