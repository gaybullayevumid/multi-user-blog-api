from rest_framework import serializers
from .models import Comments


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comments
        fields = ["id", "post", "author", "content", "created_at", "updated_at"]
        read_only_fields = ["author", "post"]
