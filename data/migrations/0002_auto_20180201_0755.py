# Generated by Django 2.0.1 on 2018-02-01 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='contact',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
