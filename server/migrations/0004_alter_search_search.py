# Generated by Django 3.2.8 on 2021-10-13 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20211012_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='search',
            field=models.CharField(default='', max_length=50),
        ),
    ]