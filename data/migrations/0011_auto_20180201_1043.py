# Generated by Django 2.0.1 on 2018-02-01 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_auto_20180201_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertiser',
            name='avatar',
            field=models.ImageField(upload_to='img'),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 10, 43, 30, 656674), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 10, 43, 30, 656694), verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='avatar',
            field=models.ImageField(upload_to='img'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 10, 43, 30, 658719), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 10, 43, 30, 658737), verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 10, 43, 30, 661136), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 10, 43, 30, 661154), verbose_name='Updated'),
        ),
    ]
