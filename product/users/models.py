from django.contrib.auth.models import AbstractUser
from django.db import models
from ..courses.models import Course


class CustomUser(AbstractUser):
    """Кастомная модель пользователя - студента."""

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=250,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.get_full_name()


class Balance(models.Model):
    """Модель баланса пользователя."""
    # TODO

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Студент')

    amount = models.DecimalField(
        verbose_name='Баланс',
        decimal_places=2,
        max_digits=8,
        default=1000.00,
        min_value=0.00,

    )

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
        ordering = ('-id',)


class Subscription(models.Model):
    """Модель подписки пользователя на курс."""

    # TODO

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс')

    student = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Студент')

    has_accees = models.BooleanField(
        default=False,
        verbose_name='Открыт доступ'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)
