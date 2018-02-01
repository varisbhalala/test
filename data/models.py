from django.db import models
import datetime

# Create your models here.
from django.db import models


class Advertisement(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    slot = models.ForeignKey('Slot', models.DO_NOTHING)
    advertiser = models.ForeignKey('Advertiser', models.DO_NOTHING, db_column='Advertiser_id')  # Field name made lowercase.
    upload = models.ForeignKey('Upload', models.DO_NOTHING, db_column='Upload_id')  # Field name made lowercase.
    board = models.ForeignKey('Board', models.DO_NOTHING, db_column='Board_id')  # Field name made lowercase.
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()



class Advertiser(models.Model):
    name = models.TextField()
    contact = models.BigIntegerField(null=True,blank=True)
    email = models.TextField()
    avatar = models.ImageField(upload_to = "advertiser" ,default="/Users/varis.bhalala/Desktop/digi_repository/static/img/dummy.jpg")
    company_name = models.TextField()
    company_address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    created_at = models.DateTimeField('Created', default=datetime.datetime.now())
    updated_at = models.DateTimeField('Updated', default=datetime.datetime.now())




class Board(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)
    street = models.TextField()
    area = models.TextField()
    city = models.TextField()
    state = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='Publisher_id')  # Field name made lowercase.




class Log(models.Model):
    timestamp = models.DateTimeField()
    created_at = models.IntegerField()
    advertisement = models.ForeignKey(Advertisement, models.DO_NOTHING, db_column='Advertisement_id')  # Field name made lowercase.



class Payment(models.Model):
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='Publisher_id')  # Field name made lowercase.
    advertiser = models.ForeignKey(Advertiser, models.DO_NOTHING, db_column='Advertiser_id')  # Field name made lowercase.
    plan = models.ForeignKey('Plan', models.DO_NOTHING)
    price = models.FloatField()
    service_tax_ratio = models.FloatField()
    service_tax = models.FloatField()
    total_amount = models.FloatField()
    trnsaction_id = models.IntegerField()
    transaction_type = models.TextField()
    is_paid = models.IntegerField()
    pay_log = models.TextField()
    created_at = models.DateTimeField()


class Publisher(models.Model):
    name = models.TextField()
    contact = models.BigIntegerField(null=True,blank=True)
    email = models.TextField()
    avatar = models.ImageField(upload_to = "publisher" ,default="/Users/varis.bhalala/Desktop/digi_repository/static/img/dummy.jpg")
    company_name = models.TextField()
    company_address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    created_at = models.DateTimeField('Created', default=datetime.datetime.now())
    updated_at = models.DateTimeField('Updated', default=datetime.datetime.now())



class Upload(models.Model):
    type = models.TextField()
    location = models.TextField()
    upload_date = models.DateTimeField()
    current_state = models.IntegerField()
    seconds = models.BigIntegerField()
    upload_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    advertiser = models.ForeignKey(Advertiser, models.DO_NOTHING, db_column='Advertiser_id')  # Field name made lowercase.





class Plan(models.Model):
    board = models.ForeignKey(Board, models.DO_NOTHING, db_column='Board_id')  # Field name made lowercase.
    publisher = models.ForeignKey(Publisher, models.DO_NOTHING, db_column='Publisher_id')  # Field name made lowercase.
    slot = models.ForeignKey('Slot', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()




class RequestBoard(models.Model):
    advertiser = models.ForeignKey(Advertiser, models.DO_NOTHING, db_column='Advertiser_id')  # Field name made lowercase.
    publisher = models.ForeignKey(Publisher, models.DO_NOTHING, db_column='Publisher_id')  # Field name made lowercase.
    board = models.ForeignKey(Board, models.DO_NOTHING, db_column='Board_id')  # Field name made lowercase.
    slot = models.ForeignKey('Slot', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()



class Slot(models.Model):
    publisher = models.ForeignKey(Publisher, models.DO_NOTHING, db_column='Publisher_id')  # Field name made lowercase.
    from_field = models.TimeField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.TimeField()
    total = models.TimeField()
    slot_price = models.IntegerField()
    created_at = models.IntegerField()
    updated_at = models.IntegerField()


class User(models.Model):
    username = models.CharField(unique=True, max_length=10)
    password = models.TextField()
    created_at = models.DateTimeField('Created', default=datetime.datetime.now())
    updated_at = models.DateTimeField('Updated', default=datetime.datetime.now())
    role = models.TextField()
    uid = models.IntegerField()




class Test(models.Model):
    advertiser = models.ForeignKey(Advertiser, models.DO_NOTHING, db_column='Advertiser_id')  # Field name made lowercase.
    publisher = models.ForeignKey(Publisher, models.DO_NOTHING, db_column='Publisher_id')  # Field name made lowercase.
    board = models.ForeignKey(Board, models.DO_NOTHING, db_column='Board_id')  # Field name made lowercase.
    slot = models.ForeignKey('Slot', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
