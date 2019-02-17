from django.urls import path
from .views import *


urlpatterns = [
    path('', balances_list, name='balances_list_url'),
    path('balance/<str:slug>/', BalanceDetail.as_view(), name='balance_deatail_url'),
    path('accounts/', accounts_list, name='account_list_url'),
    path('account/<str:slug>/', AccountDetail.as_view(), name='account_deatail_url'),
]