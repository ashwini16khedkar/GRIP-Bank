from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    email = models.CharField(max_length=100,blank=False,null=False)
    bank_balance = models.IntegerField(default=0)

class TransactionHistory(models.Model):
    sender = models.ForeignKey(User,blank=False,null=False,on_delete=models.CASCADE,related_name="sender")
    receiver = models.ForeignKey(User,blank=False,null=False,on_delete=models.CASCADE,related_name="receiver")
    amount = models.IntegerField(default=0)
    datetime = models.DateTimeField()

class ContactUs(models.Model):
    email = models.CharField(max_length=50,blank=False,null=False)
    about = models.CharField(max_length=100,blank=False,null=False)
    concern = models.CharField(max_length=150,blank=False,null=False)

