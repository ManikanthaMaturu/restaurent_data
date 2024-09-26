from django.shortcuts import render

# Create your views here.


from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework.response import Response
from datetime import datetime, timedelta


# ===============Owner Registration API ===================

class ownerPostAPI(GenericAPIView):
    serializer_class = OwnerSerializers

    def post(self, request):
        
        owner_data = self.get_serializer(data = request.data)
        owner_data.is_valid(raise_exception = True)
        owner_data.save()

        result = {
            'Message' : "Owner registration Success",
            'Result' : owner_data.data,
            'Hash Error' : False,
            'Status' : 200
        }

        return Response(result)
    

# ===================Add Restaurent to the Owner POST API======================


class RestaurentPostAPI(GenericAPIView):
    serializer_class = RestaurentSerializers

    def post(self, request):
        
        restaurent_data = self.get_serializer(data = request.data)
        restaurent_data.is_valid(raise_exception = True)
        restaurent_data.save()


        result = {
            'Message' : "restaurent added to owner",
            'Result' : restaurent_data.data,
            'Hash Error' : False,
            'Status' : 200
        }

        return Response(result)
    
# =========================Items added to available Restaurents=====================================
    

class ItemPostAPI(GenericAPIView):
    serializer_class = ItemSerializers

    def post(self, request):

        RestaurentID = request.data.get('RestaurentID')

        items_data = self.get_serializer(data = request.data)
        items_data.is_valid(raise_exception = True)
        items_data.save()


        items_list = ItemModel.objects.filter(RestaurentID = RestaurentID)


        result = {
            'Message' : "Custmur Registration Success",
            'Result' : ItemSerializers(items_list, many = True).data,
            'Hash Error' : False,
            'Status' : 200
        }
        return Response(result)
    
# =========================Get All Items from restaurent ID =====================================

class GetItems(GenericAPIView):
    serializer_class = ItemSerializers


    def get(self, request, RestaurentID):
            items_list = ItemModel.objects.filter(RestaurentID = RestaurentID)

            result = {
                'Message' : "Custmur Registration Success",
                'Result' : ItemSerializers(items_list, many = True).data,
                'Hash Error' : False,
                'Status' : 200
            }
            return Response(result)


# =========================Customur Registration POST API ==============================

class CustomurRegistrationPostAPI(GenericAPIView):
    serializer_class = CustomurRegistrationSerializers

    def post(self, request):
        
        customur_data = self.get_serializer(data = request.data)
        customur_data.is_valid(raise_exception = True)
        customur_data.save()


        result = {
            'Message' : "Custmur Registration Success",
            'Result' : customur_data.data,
            'Hash Error' : False,
            'Status' : 200
        }

        return Response(result)
    
# ======================Items Orders===================


class OrderItemsPOST(GenericAPIView):
    serializer_class = OrderItemsSerializers

    def post(self, request):
        itemID = request.data.get('itemID')
        CustomurID = request.data.get('CustomurID')

        orders_list = OrderItemsModels.objects.filter(itemID = itemID, CustomurID = CustomurID)
        if orders_list:
            current_datetime = datetime.today()

            for orders_list_loop in orders_list:
                created_on = orders_list_loop.created_on
                created_on_na = created_on.replace(tzinfo=None)
                if current_datetime < created_on_na + timedelta(days = 1):
                    message = "You have already added same itme today"
                    data_exists = True
                else:
                    message = "Succuess"
                    data_exists = False

                if data_exists == True:
                    break
            
            
            if message == "Succuess":
                ordered_data = self.get_serializer(data = request.data)
                ordered_data.is_valid(raise_exception = True)
                ordered_data.save()

                result = {
                    'Message' : "Your Order is added",
                    'Result' : ordered_data.data,
                    'Hash Error' : False,
                    'Status' : 200
                }

                return Response(result)
            else: 
                result = {
                    'Message' : message,
                    'Result' : [],
                    'Hash Error' : False,
                    'Status' : 400
                }

                return Response(result)
            
        else:
            ordered_data = self.get_serializer(data = request.data)
            ordered_data.is_valid(raise_exception = True)
            ordered_data.save()

            result = {
                'Message' : "Your Order is added",
                'Result' : ordered_data.data,
                'Hash Error' : False,
                'Status' : 200
            }

            return Response(result)


# ==============================================


class GetOrders(GenericAPIView):
    serializer_class = GetOrderItemsSerializers


    def get(self, request, CustomurID):
            Orders_list = OrderItemsModels.objects.filter(CustomurID = CustomurID)

            result = {
                'Message' : "Your Orders",
                'Result' : GetOrderItemsSerializers(Orders_list, many = True).data,
                'Hash Error' : False,
                'Status' : 200
            }
            return Response(result)





