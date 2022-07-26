from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "api.v1"

v1_router = DefaultRouter()
v1_router.register("posts", views.PostViewSet, basename="api_posts")
v1_router.register("groups", views.GroupViewSet, basename="api_groups")
v1_router.register("follow", views.FollowViewSet, basename="api_follow")
v1_router.register(
    r"posts/(?P<post_id>\d+)/comments",
    views.CommentViewSet,
    basename="api-comments",
)

urlpatterns = [
    path("v1/", include("djoser.urls.jwt")),
    path("v1/", include(v1_router.urls)),
]
