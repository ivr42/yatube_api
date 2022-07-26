from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        verbose_name="Название сообщества",
        help_text="Введите название сообщества",
        max_length=200,
    )
    slug = models.SlugField(
        unique=True,
        help_text="Задайте slug",
    )
    description = models.TextField(
        verbose_name="Описание сообщества",
        help_text="Введите описание сообщества",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сообщество"
        verbose_name_plural = "Сообщества"


class Post(models.Model):
    text = models.TextField(
        verbose_name="Текст сообщения",
        help_text="Введите текст сообщения",
    )
    pub_date = models.DateTimeField(
        verbose_name="Дата и время публикации",
        auto_now_add=True,
        help_text="Дата и время публикации: автоматическое поле",
    )
    author = models.ForeignKey(
        User,
        verbose_name="Автор сообщения",
        on_delete=models.CASCADE,
        related_name="posts",
        help_text="Автор сообщения: автоматическое поле",
    )
    image = models.ImageField(
        upload_to="posts/",
        null=True,
        blank=True,
        verbose_name="Картинка",
        help_text="Добавьте картинку (по желанию)",
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True,
        verbose_name="Сообщество",
        help_text="Укажите сообщество",
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )


class Follow(models.Model):
    following = models.ForeignKey(
        User,
        verbose_name="Автор сообщений",
        on_delete=models.CASCADE,
        related_name="following",
        help_text="Укажите автора сообщений,"
        "на которого хотите подписаться/отписаться",
    )
    user = models.ForeignKey(
        User,
        verbose_name="Подписчик",
        on_delete=models.CASCADE,
        related_name="follower",
        help_text="Подписчик: автоматическое поле",
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = [
            models.UniqueConstraint(
                fields=["following", "user"], name="unique_following"
            )
        ]

    def __str__(self):
        return f"{self.following} followed by {self.user}"
