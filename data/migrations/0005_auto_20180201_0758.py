# Generated by Django 2.0.1 on 2018-02-01 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20180201_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertiser',
            name='avatar',
            field=models.FileField(upload_to='avatar/advertiser/'),
        ),
    ]