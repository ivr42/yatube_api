from posts.models import Comment, Group, Post
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField, SlugRelatedField


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False, read_only=True, slug_field="username"
    )
    post = PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        fields = "__all__"
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
