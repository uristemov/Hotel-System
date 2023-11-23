
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Registration(models.Model):
#     username = models.CharField(primary_key=True, max_length=50)
#     password = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'registration'

# class Card(models.Model):
#     card_id = models.BigIntegerField(primary_key=True)
#     card_number = models.CharField(max_length=50, blank=True, null=True)
#     balance = models.BigIntegerField(blank=True, null=True)
#     card_cvv = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'card'
    
# class Users(models.Model):
#     user = models.OneToOneField(User)
#     # user_id = models.BigIntegerField(primary_key=True)
#     # username =models.CharField(max_length=50, blank=True, null=True) 
#     # firstname = models.CharField(max_length=50, blank=True, null=True)
#     # lastname = models.CharField(max_length=50, blank=True, null=True)
#     # email = models.CharField(max_length=50, blank=True, null=True)
#     # card = models.ForeignKey(Card, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'users'



