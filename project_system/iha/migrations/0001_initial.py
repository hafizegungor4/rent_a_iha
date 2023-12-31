# Generated by Django 4.1.7 on 2023-09-08 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='İha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('marka', models.CharField(blank=True, max_length=100)),
                ('model', models.CharField(blank=True, max_length=1000)),
                ('ağırlık', models.FloatField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'IHA',
                'verbose_name_plural': 'Iha List',
                'db_table': 'iha',
            },
        ),
    ]
