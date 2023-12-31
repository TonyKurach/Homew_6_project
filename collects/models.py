from django.db import models

# встроенная модель пользователя
# нужна для авторов сообщений
from django.contrib.auth.models import User
# тип "временнАя зона" для получения текущего времени
from django.utils import timezone



class Collect(models.Model):
    collect_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')


class Option(models.Model):
    collect = models.ForeignKey(Collect, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    correct = models.BooleanField(default=False)


class Message(models.Model):
    chat = models.ForeignKey(
        Collect,
        verbose_name='Чат под вопросом',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь', on_delete=models.CASCADE)
    message = models.TextField('Сообщение')
    pub_date = models.DateTimeField(
        'Дата сообщения',
        default=timezone.now)

class Mark(models.Model):
    collect = models.ForeignKey(
        Collect,
        verbose_name='Вопрос',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь', on_delete=models.CASCADE)
    mark = models.IntegerField(
        verbose_name='Оценка')
    pub_date = models.DateTimeField(
        'Дата оценки',
        default=timezone.now)



