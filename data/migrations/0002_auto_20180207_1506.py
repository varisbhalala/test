# Generated by Django 2.0.1 on 2018-02-07 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertiser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 6, 2, 813359), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 6, 2, 813381), verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 6, 2, 813944), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='board',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 6, 2, 813963), verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 6, 2, 815437), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 6, 2, 815454), verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 6, 2, 817869), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 6, 2, 817886), verbose_name='Updated'),
        ),
    ]
