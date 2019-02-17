from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Currency(models.Model):
    object_name = models.CharField(max_length=128, db_index=True)
    description = models.TextField(blank=True, db_index=True)
    slug = models.SlugField(max_length=8, unique=True)
    code = models.CharField(max_length=8, db_index=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    #todo сделать возможность редактирования валюты, пока все через админку или shell
    #     def get_absolute_url(self):
    #         return reverse('ccy_deatail_url', kwargs={'slug': self.slug})

    # переопределен вывод метода STR для удобства
    def __str__(self):
        return '{}'.format(self.object_name)

    def __unicode__(self):
        return '{}'.format(self.object_name)

#Модель для описания баланаса
#todo связать модель с пользователем!
class Balance(models.Model):
    object_name = models.CharField(max_length=256, db_index=True)
    description = models.TextField(blank=True, db_index=True)
    slug = models.SlugField(max_length=256, unique=True)
    ccy = models.ForeignKey('Currency',
                            on_delete=models.CASCADE,
                            related_name='balances',
                            related_query_name='balance',
                            default=1)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    #создали метод в стиле "соглашение django" для автогенерации url
    def get_absolute_url(self):
        return reverse('balance_deatail_url', kwargs={'slug':self.slug})

    #переопределен вывод метода STR для удобства
    def __str__(self):
        return '{}'.format(self.object_name)

    def __unicode__(self):
        return '{}'.format(self.object_name)

#Модель для описания акаунта
#todo type - посмотреть, может переопределить Field, может сделать отдельной моделью
class Account(models.Model):
    object_name = models.CharField(max_length=256, db_index=True)
    description = models.TextField(blank=True, db_index=True)
    slug = models.SlugField(max_length=256, unique=True)
    type = models.CharField(max_length=256, db_index=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance = models.ForeignKey('Balance',
                                on_delete=models.CASCADE,
                                related_name='accounts',
                                related_query_name='account'
                                )
    ccy = models.ForeignKey('Currency',
                            on_delete=models.CASCADE,
                            related_name='accounts',
                            related_query_name='account',
                            default=1)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('account_deatail_url', kwargs={'slug':self.slug})

    #переопределен вывод метода STR для удобства
    def __str__(self):
        return '{}'.format(self.object_name)

    def __unicode__(self):
        return '{}'.format(self.object_name)