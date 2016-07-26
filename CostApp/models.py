from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField('Категория',max_length=200)

    def __str__(self):
        return self.name


class Cost(models.Model):
    name = models.CharField('Описание',max_length=200)
    price = models.IntegerField('Расходы')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    priority = models.IntegerField('Приоритет')
    user = models.CharField('Пользователь',max_length=200)
    date = models.DateField('Дата')

    def __str__(self):
        return self.name
