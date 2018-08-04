from django.db import models
import datetime

# Create your models here.

class Blower(models.Model):
    blow_id = models.IntegerField(primary_key=True,default=1)
    blow_status = models.IntegerField(default=0)
    currenttime = models.DateTimeField(default=datetime.datetime.now())
    update_time = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'blower'


class Door(models.Model):
    door_id = models.IntegerField(primary_key=True,default=1)
    door_status = models.IntegerField(default=0)
    currenttime = models.DateTimeField(default=datetime.datetime.now())
    update_time = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'door'
    def __str__(self):
        return str(self.door_id)


class Enhistory(models.Model):
    h_id = models.AutoField(primary_key=True)
    h_temperature = models.FloatField(default=0)
    h_humidity = models.FloatField(default=0)
    h_co2 = models.FloatField(default=0)
    h_pm = models.FloatField(default=0)
    currenttime = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'enhistory'

    def __str__(self):
        return str(self.h_temperature)


class Environment(models.Model):
    e_id = models.IntegerField(primary_key=True,default=1)
    e_temperature = models.FloatField(default=0)
    e_humidity = models.FloatField(default=0)
    e_co2 = models.FloatField(default=0)
    e_pm = models.FloatField(default=0)
    e_fire = models.IntegerField(default=0)
    e_infrared = models.IntegerField(default=0)
    e_ch4 = models.IntegerField(default=0)
    e_smoke = models.IntegerField(default=0)
    currenttime = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'environment'


class Homeuser(models.Model):
    u_id = models.IntegerField(primary_key=True,default=1)
    u_name = models.CharField(max_length=30)
    u_admin = models.CharField(max_length=50)
    u_password = models.CharField(max_length=30)
    currenttime = models.DateTimeField(default=datetime.datetime.now())
    update_time = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'homeuser'


class Led(models.Model):
    led_id = models.IntegerField(primary_key=True,default=1)
    led_status = models.IntegerField(default=0)
    currenttime = models.DateTimeField(default=datetime.datetime.now())
    update_time = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'led'
    def __str__(self):
        return str(self.led_id)



class Threshold(models.Model):
    t_id = models.IntegerField(primary_key=True,default=1)
    t_temperature = models.FloatField(default=28)
    t_humidity = models.FloatField(default=65)
    t_co2 = models.FloatField(default=38)
    t_pm = models.FloatField(default=100)
    currenttime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'threshold'