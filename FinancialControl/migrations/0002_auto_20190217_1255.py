# Generated by Django 2.1.7 on 2019-02-17 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinancialControl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]