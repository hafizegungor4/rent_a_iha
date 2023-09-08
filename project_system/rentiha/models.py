from django.db import models


# Create your models here.
class RentIha(models.Model):
    member = models.ForeignKey('account.MyUser', on_delete=models.CASCADE,
                               null=False, blank=False)
    iha = models.ForeignKey('iha.İha', on_delete=models.CASCADE,
                            null=False, blank=False)
    rent_start_date = models.DateTimeField(null=True, blank=True)
    rent_end_date = models.DateTimeField(null=True, blank=True)
    is_renter = models.BooleanField(default=False)


    class Meta:
        db_table = 'rentiha'
        verbose_name = 'Rent a Iha'
        verbose_name_plural = 'Rent a Iha'
        unique_together = ('member', 'iha')

    def __str__(self):
        return "%s - %s" % (self.iha.code,
                            self.member.identication_number)
