# Generated by Django 2.1.7 on 2019-02-17 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinancialControl', '0007_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='ccy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='accounts', related_query_name='account', to='FinancialControl.Currency'),
        ),
        migrations.AddField(
            model_name='balance',
            name='ccy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='balances', related_query_name='balance', to='FinancialControl.Currency'),
        ),
    ]