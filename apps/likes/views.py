from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Like
from apps.posts.models import Post

# Create your views here.


class ToggleLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            like.delete()
            return Response(
                {"message": "Like removed", "liked": False},
                status=status.HTTP_200_OK
            )

        return Response(
            {"message": "Post liked", "liked": True},
            status=status.HTTP_201_CREATED
        )
