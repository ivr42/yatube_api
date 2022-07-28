from posts.models import Comment, Follow, Group, Post, User
from rest_framework import filters, mixins, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(post=post, author=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["following__username"]

    def get_queryset(self, *args, **kwargs):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        following = get_object_or_404(
            User, username=self.request.data.get("following")
        )
        if following == self.request.user:
            raise ValidationError(
                {"detail": "Пользователь не может быть подписан сам на себя"}
            )
        if Follow.objects.filter(
            following=following,
            user=self.request.user,
        ).exists():
            raise ValidationError({"detail": "Такая подписка уже существует"})

        serializer.save(user=self.request.user)
