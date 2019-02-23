from django.http import HttpResponse
from django.shortcuts import redirect

def redirect_financial_control(request):
    return redirect('balances_list_url', permanent=True)