


from django.urls import path
from .views import *



urlpatterns = [

    path('OwnerRegi/', ownerPostAPI.as_view(), name = "Owner Registration"),
    path('RestaurentPostAPI/', RestaurentPostAPI.as_view(), name = "RestaurentPostAPI"),
    path('CustomurRegistrationPostAPI/', CustomurRegistrationPostAPI.as_view(), name = "CustomurRegistrationPostAPI"),
    path('ItemPostAPI/', ItemPostAPI.as_view(), name = "ItemPostAPI"),
    path('OrderItemsPOST/', OrderItemsPOST.as_view(), name = "OrderItemsPOST"),
    path('GetItems/<int:RestaurentID>', GetItems.as_view(), name = "GetItems"),
    path('GetOrders/<int:CustomurID>', GetOrders.as_view(), name = "GetOrders"),

]