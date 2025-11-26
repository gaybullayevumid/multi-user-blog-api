from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    likes_count = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'image', 'created_at']

    def get_likes_count(self, obj):
        return obj.likes.count()