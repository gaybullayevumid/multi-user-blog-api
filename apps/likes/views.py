from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Like
from apps.posts.models import Post

# Create your views here.


class ToggleLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        user = request.user
        
        like = Like.objects.filter(user=user, post=post).first()

        if like:
            like.delete()
            return Response({"message": "Like removed"}, status=status.HTTP_200_OK)
        
        Like.objects.create(user=user, post=post)
        return Response({"message": "Post Liked"}, status=status.HTTP_201_CREATED)