from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Cost(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    priority = models.IntegerField()
    user = models.CharField(max_length=200)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
