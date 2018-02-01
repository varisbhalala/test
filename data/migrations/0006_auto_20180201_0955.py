# Generated by Django 2.0.1 on 2018-02-01 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20180201_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertiser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 9, 55, 14, 894427), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 9, 55, 14, 894448), verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='avatar',
            field=models.ImageField(upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 9, 55, 14, 896414), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 9, 55, 14, 896434), verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 9, 55, 14, 898889), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 1, 9, 55, 14, 898907), verbose_name='Updated'),
        ),
    ]
