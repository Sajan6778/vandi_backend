from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Credentials(models.Model):
    Gender=[('male',"Male"),("female",'Female'),('other','others')]
    category=[("customer","customer"),('worker','worker'),("transport","transport")]
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=Gender)
    phone_number=models.CharField(max_length=20)
    pincode=models.IntegerField()
    categories=models.CharField(max_length=50,choices=category)
    area=models.CharField(max_length=50)
    

