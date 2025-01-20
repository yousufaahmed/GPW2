from django.db import models


class AmountType(models.Model):
    name = models.CharField(max_length=200, primary_key=True)

class ItemType(models.Model):
    unique_barcode = models.IntegerField(max_length=100,primary_key=True)
    name = models.CharField(max_length=200)
    amount_type = models.ForeignKey(AmountType, max_length=200, on_delete=models.CASCADE)

class IndividualItems(models.Model):
    id = models.IntegerField(max_length=100,primary_key=True)
    expiration_date = models.DateField()
    type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    amount = models.IntegerField()

class ShoppingList(models.Model):
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    amount = models.IntegerField()