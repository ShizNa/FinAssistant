# Generated by Django 2.1.7 on 2019-02-16 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_created=True)),
                ('object_name', models.CharField(db_index=True, max_length=256)),
                ('description', models.TextField(blank=True, db_index=True)),
                ('slug', models.SlugField(max_length=256, unique=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
