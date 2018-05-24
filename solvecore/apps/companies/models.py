
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):
    """
    """

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='companies'
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    current_accounting_firm = models.ForeignKey(
        'companies.CurrentAccountingFirm',
        on_delete=models.SET_NULL,
        related_name='companies',
        null=True, blank=True
    )
    banks = models.ForeignKey('companies.Bank',
        on_delete=models.SET_NULL,
        related_name='companies',
        null=True, blank=True
    )

    def __str__(self):
        return "{id}: {name}".format(id=self.id, name=self.name)

    class Meta:
        db_table = 'company'
        verbose_name = ('company',)
        verbose_name_plural = _('companies',)


class CompanyFarmBaseModel(models.Model):
    """
    """

    name = models.CharField(max_length=255)
    farm_type = models.ForeignKey('companies.FarmType',
        on_delete=models.PROTECT,
        related_name='company_farm'
    )
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE,
        related_name='companyfarms')

    def __str__(self):
        return "{id}: {name}".format(id=self.id, name=self.name)

    class Meta:
        abstract = True


class CompanyFarm(CompanyFarmBaseModel):
    """
    """

    pass

    class Meta:
        db_table = 'companyfarm'
        verbose_name = ('companyfarm',)
        verbose_name_plural = ('companyfarms',)


class FarmType(models.Model):
    """
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return "{id}: {name}".format(id=self.id, name=self.name)

    class Meta:
        db_table = 'farmtype'
        verbose_name = _('farmtype')
        verbose_name_plural = _('farmtypes')


class Bank(models.Model):
    """
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return "{id}: {name}".format(id=self.id, name=self.name)

    class Meta:
        db_table = 'bank'
        verbose_name = ('bank',)
        verbose_name_plural = ('banks',)


class CurrentAccountingFirm(models.Model):
    """
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return "{id}: {name}".format(id=self.id, name=self.name)

    class Meta:
        db_table = 'currentaccountingfirm'
        verbose_name = ('currentaccountingfirm',)
        verbose_name_plural = ('currentaccountingfirms',)
