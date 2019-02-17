from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .models import Balance, Account
from .utils import ObjectDetailMixin

# Create your views here.

class BalanceDetail(ObjectDetailMixin,View):
    model = Balance
    template = 'FinancialControl/balance_detail.html'


class AccountDetail(ObjectDetailMixin,View):
    model = Account
    template = 'FinancialControl/account_detail.html'


def balances_list(request):
    balances = Balance.objects.all()
    return render(request, 'FinancialControl/balance.html', context={'balances': balances})

def accounts_list(request):
    accounts = Account.objects.all()
    return render(request,'FinancialControl/account.html', context={'accounts':accounts})