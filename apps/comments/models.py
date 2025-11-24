from django.db import models
from django.conf import settings
from posts.models import Post

# Create your models here.


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=False)
    updated_at = models.DateField(auto_now=False)


    def __str__(self):
        return f"{self.author.username} -> {self.post.title[:20]}"

