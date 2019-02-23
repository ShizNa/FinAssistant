from django.views.generic import View

from .utils import *
from .forms import *


class BalanceAdd(ObjectAddMixin, View):
    model_form = BalanceForm
    template = 'FinancialControl/balance_add.html'


class BalanceUpdate(ObjectUpdateMixin, View):
    model = Balance
    model_form = BalanceForm
    template = 'FinancialControl/balance_update.html'

class BalanceDelete(ObjectDeleteMixin, View):
    model = Balance
    template = 'FinancialControl/balance_delete.html'
    redirect_url = 'balances_list_url'


class BalanceDetail(ObjectDetailMixin, View):
    model = Balance
    template = 'FinancialControl/balance_detail.html'


def balances_list(request):
    return render(request, 'FinancialControl/balance.html', context={'balances': Balance.objects.all()})


class AccountAdd(ObjectAddMixin, View):
    model_form = AccountForm
    template = 'FinancialControl/account_add.html'


class AccountUpdate(ObjectUpdateMixin, View):
    model = Account
    model_form = AccountForm
    template = 'FinancialControl/account_update.html'


class AccountDelete(ObjectDeleteMixin, View):
    model = Account
    template = 'FinancialControl/account_delete.html'
    redirect_url = 'account_list_url'


class AccountDetail(ObjectDetailMixin, View):
    model = Account
    template = 'FinancialControl/account_detail.html'


def accounts_list(request):
    return render(request, 'FinancialControl/account.html', context={'accounts': Account.objects.all()})
