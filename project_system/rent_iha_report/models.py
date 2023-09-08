from django.db import models
# Create your models here.
class RentIhaReport(models.Model):
    member = models.ForeignKey('account.MyUser', on_delete=models.CASCADE,
                                null=False, blank=False)
    iha = models.ForeignKey('rentiha.RentIha', on_delete=models.CASCADE,
                                null=False, blank=False)

    class Meta:
        db_table = 'rent_iha_report'
        verbose_name = 'Rent Iha Report'
        verbose_name_plural = 'Rent Iha Reports'
        unique_together = ( 'iha','member')

    def __str__(self):
        return f"{self.iha} " \
               f"{self.member.first_name} " \
