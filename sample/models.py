from django.db import models

class Data(models.Model):
    Name=models.CharField(max_length=20,default="")
    Email=models.CharField(max_length=20,default="")
    Mobile=models.CharField(max_length=20,default="")
    Message=models.CharField(max_length=20,default="")

    class Meta:
        db_table='port'


