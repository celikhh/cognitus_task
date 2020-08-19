from django.db import models


class Data(models.Model):
    label = models.TextField()
    text = models.TextField()

    class Meta:
        verbose_name = "Data"
        verbose_name_plural = "Data"
        ordering = ['pk']

    def __str__(self):
        return str(self.pk)
