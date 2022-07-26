from django.contrib import admin

from .models import Comment, Follow, Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


class FollowAdmin(admin.ModelAdmin):
    list_display = ("pk", "following", "user")
    list_editable = (
        "following",
        "user",
    )
    list_filter = ("user", "following")


class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "slug", "title", "description")
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Group, GroupAdmin)
