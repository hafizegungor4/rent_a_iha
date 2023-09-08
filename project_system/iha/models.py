from django.db import models


class İha(models.Model):

    code = models.CharField(unique=True, null=False,
                            blank=False, max_length=10)
    marka = models.CharField(null=False, blank=True, max_length=100)
    model = models.CharField(null=False, blank=True, max_length=1000)
    ağırlık = models.FloatField(null=True, blank=True)
    category = models.CharField(null=True, blank=True, max_length=100)
    description = models.CharField(null=True, blank=True, max_length=1000)

    class Meta:
        db_table = 'iha'
        verbose_name = 'IHA'
        verbose_name_plural = 'Iha List'

    def __str__(self):
        return self.code + " " + self.marka + " " + self.model
