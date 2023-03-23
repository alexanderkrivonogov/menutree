from django.db import models


class MenuItem(models.Model):
    parent = models.ForeignKey('self', related_name='children', verbose_name='Родитель', null=True, blank=True,
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name
