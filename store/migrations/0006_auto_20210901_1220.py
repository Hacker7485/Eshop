# Generated by Django 2.2.22 on 2021-09-01 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210901_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
    ]