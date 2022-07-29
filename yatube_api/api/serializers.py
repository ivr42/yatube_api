from posts.models import Comment, Follow, Group, Post, User
from rest_framework import relations, serializers, validators

from .validators import AllDifferentValidator


class PostSerializer(serializers.ModelSerializer):
    author = relations.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = relations.SlugRelatedField(
        required=False, read_only=True, slug_field="username"
    )
    post = relations.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        fields = "__all__"
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class FollowSerializer(serializers.ModelSerializer):
    user = relations.SlugRelatedField(
        required=False,
        read_only=True,
        slug_field="username",
        default=serializers.CurrentUserDefault(),
    )
    following = relations.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ("user", "following")
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("user", "following"),
                message="Такая подписка уже существует",
            ),
            AllDifferentValidator(
                fields=("user", "following"),
                message="Пользователь не может быть подписан сам на себя",
            ),
        ]
