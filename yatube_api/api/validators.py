from typing import Optional

from rest_framework.validators import ValidationError


class AllDifferentValidator:
    """Проверяет на уникальность значения полей.

    Attributes:
        fields(list[str]): список полей для валидации
        message(str): текст сообщения об ошибке
    """

    default_message = "Все значения должны быть разными"

    def __init__(
        self, fields: list[str], message: Optional[str] = None
    ) -> None:
        self.fields = fields
        self.message = message or self.default_message

    @staticmethod
    def _all_unique(lst: list[str]) -> bool:
        """Проверяет, что все строки списка уникальны.

        Args:
            lst(list[str]): список строк для проверки

        Returns:
            bool: True - если все строки уникальны, в противном случае - False
        """

        return len(lst) == len(set(lst))

    def __call__(self, attrs):
        checked_values = [
            value for field, value in attrs.items() if field in self.fields
        ]

        if not self._all_unique(checked_values):
            raise ValidationError(self.message)
