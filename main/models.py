from django.db import models


class Corporations(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=300)
    descr = models.CharField(max_length=500)
    ovner = models.CharField(max_length=100)
    age = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Корпорация'
        verbose_name_plural = 'Корпорации'