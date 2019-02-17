# Generated by Django 2.1.7 on 2019-02-17 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinancialControl', '0004_auto_20190217_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balances', related_query_name='balance', to='FinancialControl.Balance'),
        ),
    ]