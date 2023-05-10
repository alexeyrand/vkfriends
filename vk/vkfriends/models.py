from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, verbose_name='Никнейм')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    age = models.PositiveIntegerField(verbose_name='Возраст')


    def __str__(self):
        return str(self.username)