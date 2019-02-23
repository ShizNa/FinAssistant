from django.urls import path
from .views import *

urlpatterns = [
    path('', balances_list, name='balances_list_url'),
    path('balance/add/', BalanceAdd.as_view(), name='balance_add_url'),
    path('balance/<str:slug>/', BalanceDetail.as_view(), name='balance_deatail_url'),
    path('balance/<str:slug>/update/', BalanceUpdate.as_view(), name='balance_update_url'),
    path('balance/<str:slug>/delete/', BalanceDelete.as_view(), name='balance_delete_url'),
    path('accounts/', accounts_list, name='account_list_url'),
    path('account/add/', AccountAdd.as_view(), name='account_add_url'),
    path('account/<str:slug>/', AccountDetail.as_view(), name='account_deatail_url'),
    path('account/<str:slug>/update/', AccountUpdate.as_view(), name='account_update_url'),
    path('account/<str:slug>/delete/', AccountDelete.as_view(), name='account_delete_url'),
]
