from django.db import models
from django.shortcuts import reverse
from pytils.translit import slugify
from time import time


# Generator for unic slug
def gen_slug(s):
    return slugify(s) + '-' + str(int(time()))


def get_all_accounts_summ(b):
    summ = 0
    accounts = b.accounts.all()
    for account in accounts:
        summ = summ + account.amount
    return summ
    '''вариант как суммировать. не забыть подключить библиотеку from django.db.models import Sum
    пока оставляем так, как выше написано, когда нужно будет конвертировать валюту - решим'''
    # result = b.accounts.all().aggregate(Sum('amount'))
    # return str(result['amount__sum'])


class Currency(models.Model):
    object_name = models.CharField(max_length=128, db_index=True)
    description = models.TextField(blank=True, db_index=True)
    slug = models.SlugField(max_length=8, unique=True, blank=True)
    code = models.CharField(max_length=8, db_index=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    # todo сделать возможность редактирования валюты, пока все через админку или shell
    #     def get_absolute_url(self):
    #         return reverse('ccy_deatail_url', kwargs={'slug': self.slug})

    # переопределен вывод метода STR для удобства
    def __str__(self):
        return '{}'.format(self.object_name)

    def __unicode__(self):
        return '{}'.format(self.object_name)


# Модель для описания баланаса
# todo связать модель с пользователем!
class Balance(models.Model):
    object_name = models.CharField(max_length=256, db_index=True)
    description = models.TextField(blank=True, db_index=True)
    slug = models.SlugField(max_length=256, unique=True, blank=True)
    ccy = models.ForeignKey('Currency',
                            on_delete=models.CASCADE,
                            related_name='balances',
                            related_query_name='balance',
                            default=1)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    # создали метод в стиле "соглашение django" для автогенерации url
    def get_absolute_url(self):
        return reverse('balance_deatail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('balance_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('balance_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.object_name)
        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.balance_amount = get_all_accounts_summ(self)

    # переопределен вывод метода STR для удобства
    def __str__(self):
        return '{}'.format(self.object_name)

    def __unicode__(self):
        return '{}'.format(self.object_name)


# Модель для описания акаунта
# todo type - посмотреть, может переопределить Field, может сделать отдельной моделью
class Account(models.Model):
    object_name = models.CharField(max_length=256, db_index=True)
    description = models.TextField(blank=True, db_index=True)
    slug = models.SlugField(max_length=256, unique=True, blank=True)
    type = models.CharField(max_length=8,
                            choices=(
                                ('positive', 'Positive'),
                                ('negative', 'Negative'),
                            ),
                            default='negative')
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
        return reverse('account_deatail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('account_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('account_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.object_name)
        super().save(*args, **kwargs)

    # переопределен вывод метода STR для удобства
    def __str__(self):
        return '{}'.format(self.object_name)

    def __unicode__(self):
        return '{}'.format(self.object_name)
