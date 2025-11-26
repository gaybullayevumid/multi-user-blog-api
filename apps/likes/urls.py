from django.urls import path
from .views import ToggleLikeView


urlpatterns = [
    path("posts/<int:post_id>/like/", ToggleLikeView.as_view(), name="toggle-like"),
]
