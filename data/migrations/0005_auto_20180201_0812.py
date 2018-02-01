# Generated by Django 2.0.1 on 2018-02-01 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20180201_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertiser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 8, 12, 43, 739796), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 8, 12, 43, 739816), verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 8, 12, 43, 741719), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 8, 12, 43, 741739), verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 8, 12, 43, 744064), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 8, 12, 43, 744081), verbose_name='Updated'),
        ),
    ]