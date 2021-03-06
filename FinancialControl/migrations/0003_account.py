# Generated by Django 2.1.7 on 2019-02-17 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinancialControl', '0002_auto_20190217_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_name', models.CharField(db_index=True, max_length=256)),
                ('description', models.TextField(blank=True, db_index=True)),
                ('slug', models.SlugField(max_length=256, unique=True)),
                ('type', models.CharField(db_index=True, max_length=256)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('balance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinancialControl.Balance')),
            ],
        ),
    ]
