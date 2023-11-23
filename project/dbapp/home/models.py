


from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *


# class Card(models.Model):
#     card_id = models.BigAutoField(primary_key=True)
#     card_number = models.CharField(max_length=50, blank=True, null=True)
#     balance = models.BigIntegerField(blank=True, null=True)
#     card_cvv = models.BigIntegerField(blank=True, null=True)
#     user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed=True
#         db_table = 'card'


# class City(models.Model):
#     city_id = models.BigAutoField(primary_key=True)
#     city_name = models.CharField(max_length=50, blank=True, null=True)
#     country = models.ForeignKey('Country', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed=True
#         db_table = 'city'


# class Country(models.Model):
#     country_id = models.BigAutoField(primary_key=True)
#     country_name = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'country'

# class HotelOrders(models.Model):
#     order_id = models.BigAutoField(primary_key=True)
#     hotel = models.ForeignKey('Hotels', models.DO_NOTHING, blank=True, null=True)
#     total_balance = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'hotel_orders'


# class Hotels(models.Model):
#     hotel_id = models.BigAutoField(primary_key=True)
#     hotel_photo = models.CharField(max_length=50, blank=True, null=True)
#     hotel_name = models.CharField(max_length=50, blank=True, null=True)
#     description = models.CharField(max_length=50, blank=True, null=True)
#     hotel_price = models.BigIntegerField(blank=True, null=True)
#     city_id = models.BigIntegerField(blank=True, null=True)
#     tour_id = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'hotels'

# class Tour(models.Model):
#     tour_id = models.BigAutoField(primary_key=True)
#     tour_name = models.CharField(max_length=50, blank=True, null=True)
#     tour_description = models.CharField(max_length=50, blank=True, null=True)
#     tour_price = models.BigIntegerField(blank=True, null=True)
#     city_id = models.BigIntegerField(blank=True, null=True)
#     tour_photo = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tour'


# class TourOrders(models.Model):
#     order_id = models.BigAutoField(primary_key=True)
#     tour = models.ForeignKey(Tour, models.DO_NOTHING, blank=True, null=True)
#     total_balance = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tour_orders'





# Create your models here.

class Card(models.Model):
    card_id = models.BigAutoField(primary_key=True)
    card_number = models.CharField(max_length=50, blank=True, null=True)
    balance = models.BigIntegerField(blank=True, null=True, default=100)
    card_cvv = models.BigIntegerField(blank=True, null=True)
    card_month = models.BigIntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])
    card_year = models.BigIntegerField(blank=True, null=True,validators=[MinValueValidator(2021)])
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed=True
        db_table = 'card'


class City(models.Model):
    city_id = models.BigAutoField(primary_key=True)
    city_name = models.CharField(max_length=50, blank=True, null=True)
    country = models.ForeignKey('Country', models.DO_NOTHING, blank=True, null=True)
    def __str__(self):
        return self.city_name    
    class Meta:
        managed = True
        db_table = 'city'



class Country(models.Model):
    country_id = models.BigAutoField(primary_key=True)
    country_name = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.country_name
    class Meta:
        managed=True
        db_table = 'country'

class Tour(models.Model):
    tour_id = models.BigAutoField(primary_key=True)
    tour_name = models.CharField(max_length=50, blank=True, null=True)
    tour_description = models.CharField(max_length=200, blank=True, null=True)
    tour_price = models.BigIntegerField(blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    tour_photo = models.URLField(max_length=200, blank=True, null=False)
    def __str__(self):
        return self.tour_name
    class Meta:
        managed = True
        db_table = 'tour'
class Hotels(models.Model):
    hotel_id = models.BigAutoField(primary_key=True)
    hotel_photo = models.URLField(max_length=200, blank=True, null=False)
    # hotel_photo = models.CharField(max_length=200, blank=True, null=True)
    hotel_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    # hotel_price = models.BigIntegerField(blank=True, null=True)
    city = models.ForeignKey('City', models.DO_NOTHING, blank=True, null=True, db_column='city_id')
    tour = models.ForeignKey('Tour', models.DO_NOTHING, blank=True, null=True, db_column='tour_id')
    hotel_price = models.BigIntegerField(blank=True, null=True)
    def __str__(self):
        return self.hotel_name
    # tour_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed=True
        db_table = 'hotels'




class HotelOrders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    hotel = models.ForeignKey(Hotels, models.DO_NOTHING, blank=True, null=True)
    total_balance = models.BigIntegerField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)


    class Meta:
        managed=True
        db_table = 'hotel_orders'






class TourOrders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    tour = models.ForeignKey(Tour, models.DO_NOTHING, blank=True, null=True)
    # tour_id = models.BigIntegerField(blank=True, null=True)
    total_balance = models.BigIntegerField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed=True
        db_table = 'tour_orders'







#-----------------------------------------------------------------------------
# class Card(models.Model):
#     card_id = models.BigIntegerField(primary_key=True, default= 51)
#     card_number = models.CharField(max_length=50, blank=True, null=True)
#     balance = models.BigIntegerField(blank=True, null=True, default=100)
#     card_cvv = models.BigIntegerField(blank=True, null=True)
#     user_id = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'card'    



# class City(models.Model):
#     city_id = models.BigIntegerField(primary_key=True)
#     city_name = models.CharField(max_length=50, blank=True, null=True)
#     country = models.ForeignKey('Country', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'city'


# class Country(models.Model):
#     country_id = models.BigIntegerField(primary_key=True)
#     country_name = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'country'


# class HotelOrders(models.Model):
#     order_id = models.BigIntegerField(primary_key=True)
#     hotel = models.ForeignKey('Hotels', models.DO_NOTHING, blank=True, null=True)
#     total_balance = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'hotel_orders'


# class Hotels(models.Model):
#     hotel_id = models.BigIntegerField(primary_key=True)
#     hotel_photo = models.CharField(max_length=50, blank=True, null=True)
#     hotel_name = models.CharField(max_length=50, blank=True, null=True)
#     description = models.CharField(max_length=50, blank=True, null=True)
#     hotel_price = models.BigIntegerField(blank=True, null=True)
#     # city_id = models.BigIntegerField(blank=True, null=True)
#     city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
#     # tour_id = models.BigIntegerField(blank=True, null=True)
#     tour_id = models.ForeignKey('Tour', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'hotels'

# class Tour(models.Model):
#     tour_id = models.BigIntegerField(primary_key=True)
#     tour_name = models.CharField(max_length=50, blank=True, null=True)
#     tour_description = models.CharField(max_length=50, blank=True, null=True)
#     tour_price = models.BigIntegerField(blank=True, null=True)
#     city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
#     # hotel = models.ForeignKey(Hotels, models.DO_NOTHING, blank=True, null=True)
#     tour_photo = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'tour'


# class TourOrders(models.Model):
#     order_id = models.BigIntegerField(primary_key=True)
#     tour = models.ForeignKey(Tour, models.DO_NOTHING, blank=True, null=True)
#     total_balance = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'tour_orders'


