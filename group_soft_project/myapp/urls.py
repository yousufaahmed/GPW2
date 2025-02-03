from django.urls import path
from .views import add_to_inventory

urlpatterns = [
    path('addToInventory/', add_to_inventory, name='add_to_inventory'),
]
