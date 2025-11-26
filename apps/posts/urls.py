from django.urls import path
from .views import PostListCreateView, PostDetailView

urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
