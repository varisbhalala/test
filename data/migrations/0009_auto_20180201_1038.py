# Generated by Django 2.0.1 on 2018-02-01 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20180201_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertiser',
            name='avatar',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 10, 38, 19, 674131), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 10, 38, 19, 674151), verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='avatar',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 10, 38, 19, 676193), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 10, 38, 19, 676211), verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 10, 38, 19, 678636), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 10, 38, 19, 678654), verbose_name='Updated'),
        ),
    ]
