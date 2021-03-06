# Generated by Django 2.0.1 on 2018-02-07 09:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('is_active', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contact', models.BigIntegerField(blank=True, null=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('avatar', models.ImageField(default='/Users/varis.bhalala/Desktop/digi_repository/static/img/dummy.jpg', upload_to='advertiser')),
                ('company_name', models.TextField()),
                ('company_address', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 5, 47, 789028), verbose_name='Created')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 5, 47, 789051), verbose_name='Updated')),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=8, max_digits=10)),
                ('lng', models.DecimalField(decimal_places=8, max_digits=11)),
                ('street', models.TextField()),
                ('area', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 5, 47, 789588), verbose_name='Created')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 5, 47, 789605), verbose_name='Updated')),
                ('Publisher_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('created_at', models.IntegerField()),
                ('advertisement', models.ForeignKey(db_column='Advertisement_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Advertisement')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('service_tax_ratio', models.FloatField()),
                ('service_tax', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('trnsaction_id', models.IntegerField()),
                ('transaction_type', models.TextField()),
                ('is_paid', models.IntegerField()),
                ('pay_log', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('advertiser', models.ForeignKey(db_column='Advertiser_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Advertiser')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('board', models.ForeignKey(db_column='Board_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Board')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contact', models.BigIntegerField(blank=True, null=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('avatar', models.ImageField(default='/Users/varis.bhalala/Desktop/digi_repository/static/img/dummy.jpg', upload_to='publisher')),
                ('company_name', models.TextField()),
                ('company_address', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 5, 47, 791052), verbose_name='Created')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 5, 47, 791069), verbose_name='Updated')),
            ],
        ),
        migrations.CreateModel(
            name='RequestBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('advertiser', models.ForeignKey(db_column='Advertiser_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Advertiser')),
                ('board', models.ForeignKey(db_column='Board_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Board')),
                ('publisher', models.ForeignKey(db_column='Publisher_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_field', models.TimeField(db_column='from')),
                ('to', models.TimeField()),
                ('total', models.TimeField()),
                ('slot_price', models.IntegerField()),
                ('created_at', models.IntegerField()),
                ('updated_at', models.IntegerField()),
                ('publisher', models.ForeignKey(db_column='Publisher_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('advertiser', models.ForeignKey(db_column='Advertiser_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Advertiser')),
                ('board', models.ForeignKey(db_column='Board_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Board')),
                ('publisher', models.ForeignKey(db_column='Publisher_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Publisher')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Slot')),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
                ('location', models.TextField()),
                ('upload_date', models.DateTimeField()),
                ('current_state', models.IntegerField()),
                ('seconds', models.BigIntegerField()),
                ('upload_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('advertiser', models.ForeignKey(db_column='Advertiser_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Advertiser')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.TextField()),
                ('token', models.TextField(default=None, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 5, 47, 793436), verbose_name='Created')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2018, 2, 7, 15, 5, 47, 793453), verbose_name='Updated')),
                ('role', models.TextField()),
                ('uid', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='requestboard',
            name='slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Slot'),
        ),
        migrations.AddField(
            model_name='plan',
            name='publisher',
            field=models.ForeignKey(db_column='Publisher_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Publisher'),
        ),
        migrations.AddField(
            model_name='plan',
            name='slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Slot'),
        ),
        migrations.AddField(
            model_name='payment',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Plan'),
        ),
        migrations.AddField(
            model_name='payment',
            name='publisher',
            field=models.ForeignKey(db_column='Publisher_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Publisher'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='advertiser',
            field=models.ForeignKey(db_column='Advertiser_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Advertiser'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='board',
            field=models.ForeignKey(db_column='Board_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Board'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data.Slot'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='upload',
            field=models.ForeignKey(db_column='Upload_id', on_delete=django.db.models.deletion.DO_NOTHING, to='data.Upload'),
        ),
    ]
