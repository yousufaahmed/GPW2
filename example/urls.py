from django.urls import path
from .views import add_item, add_to_shoppinglist, new_type

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/addItem', add_item, name='add-item'),
    path('api/v1/newType', new_type, name='new-type'),
    path('api/v1/addToShoppingList', add_to_shoppinglist, name='add-to-shoppinglist'),
]