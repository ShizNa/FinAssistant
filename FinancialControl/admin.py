from django.contrib import admin
from FinancialControl.models import *

# Register your models here.
# https://www.youtube.com/watch?v=_7c8jOpOZSs - чтобы в админке отображались

class CurrencyAdmin(admin.ModelAdmin):
    pass

class BalanceAdmin(admin.ModelAdmin):
    pass

class AccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Balance, BalanceAdmin)