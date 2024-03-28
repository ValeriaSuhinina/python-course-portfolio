"""
Модели для приложения "Автор".
"""
from django.db import models

from django.contrib import admin

from base.models import TimeStampMixin


class Author(TimeStampMixin):
    """
    Модель для хранения данных об авторе.
    """

    resume_url = models.URLField(
        help_text="Ссылка на резюме",
        verbose_name="Резюме",
    )
    github_url = models.URLField(
        help_text="Ссылка на GitHub",
        verbose_name="GitHub",
    )
    email = models.EmailField(
        verbose_name="Электронная почта",
    )

    class Meta:
        verbose_name_plural = "Информация об авторе"

    def __str__(self) -> str:
        return f'Объект "Автор" (id={self.pk})'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Функции панели управления для приложения "Автор".
    """

    list_display = (
        "resume_url",
        "github_url",
        "email",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )
