from rest_framework import serializers
from .models import IndividualItems, ItemType, ShoppingList

class IndividualItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualItems
        fields = ['type', 'expiration_date', 'amount']

class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = ['unique_barcode', 'name', 'amount_type']

class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ['item_type', 'amount']



