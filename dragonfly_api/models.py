from django.db import models

# python manage.py inspectdb    自动生成模型

class Constraint(models.Model):
    in_id = models.IntegerField()
    us_id = models.IntegerField()
    job = models.CharField(max_length=225)

    class Meta:
        managed = False
        db_table = 'constraint'


class Information(models.Model):
    in_id = models.AutoField(primary_key=True)
    in_title = models.CharField(max_length=255)
    in_time = models.DateTimeField()
    in_site = models.CharField(max_length=255)
    in_introduce = models.TextField()

    class Meta:
        managed = False
        db_table = 'information'


class User(models.Model):
    us_id = models.AutoField(primary_key=True)
    us_name = models.CharField(max_length=15)
    us_password = models.CharField(max_length=15)
    us_email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user'

