from rest_framework import generics, permissions
from .models import Comments
from .serailizers import CommentSerializer
from .permissions import IsCommentAuthorOrReadOnly


# Create your views here.

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id =  self.kwargs['post_id']
        return Comments.objects.filter(post_id=post_id).order_by('-created_at')


    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(author=self.request.user, post_id=post_id)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentAuthorOrReadOnly]
