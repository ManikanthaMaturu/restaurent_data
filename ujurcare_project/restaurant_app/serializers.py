
from rest_framework import serializers
from .models import *




class OwnerSerializers(serializers.ModelSerializer):
    class Meta:
        model = OwnerRegistrationModel
        fields = '__all__'



class RestaurentSerializers(serializers.ModelSerializer):
    class Meta:
        model = RestaurentModel
        fields = '__all__'



class CustomurRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomurRegistrationModel
        fields = '__all__'


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'



class OrderItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItemsModels
        fields = ['CustomurID','itemID','Quantity','SpecialInstruction']
   

class GetOrderItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItemsModels
        fields = '__all__'
