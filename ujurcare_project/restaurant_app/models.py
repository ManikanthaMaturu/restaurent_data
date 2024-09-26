from django.db import models

# Create your models here.

#  Created Owner registraion
class OwnerRegistrationModel(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50, unique=True)
    MobileNumber = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

    class Meta: 
        db_table = "Owner_registration_collection"


#  Restaurent Added to the Owner
class RestaurentModel(models.Model):
    RegistrationID = models.ForeignKey(OwnerRegistrationModel,on_delete = models.CASCADE,related_name = 'OwnerID')
    RestaurentName = models.CharField(max_length=100)
    Type = models.CharField(max_length=50)
    class Meta: 
        db_table = "restaurent_collection"



class CustomurRegistrationModel(models.Model):
    CustomurName = models.CharField(max_length=50)
    CustomurEmail = models.EmailField(max_length=50, unique=True)
    CustomurMobileNumber = models.CharField(max_length=50)
    CustomurPassword = models.CharField(max_length=50)

    class Meta: 
        db_table = "Customur_registration_collection"


# Here we can add items to the available restaurents

class ItemModel(models.Model):
    RestaurentID = models.ForeignKey(RestaurentModel,on_delete = models.CASCADE,related_name = 'restaurent_item')
    ItemName = models.CharField(max_length=500)
    Price = models.CharField(max_length=50)
    Available = models.CharField(max_length=50)

    class Meta: 
        db_table = "items_collection"


class OrderItemsModels(models.Model):

    CustomurID =  models.ForeignKey(CustomurRegistrationModel,on_delete = models.CASCADE,related_name = 'order_item')
    itemID =  models.ForeignKey(ItemModel,on_delete = models.CASCADE,related_name = 'order_item')
    Quantity = models.CharField(max_length=50)
    SpecialInstruction = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    class Meta: 
        db_table = "orders_collection"


