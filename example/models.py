from django.db import models

class AmountType(models.Model):
    name = models.CharField(primary_key=True, max_length=200)

class ItemType(models.Model):
    unique_barcode = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)
    amount_type = models.ForeignKey(AmountType, on_delete=models.CASCADE)

class IndividualItems(models.Model):
    type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    expiration_date = models.DateField()
    amount = models.IntegerField(default=0)

class ShoppingList(models.Model):
    item_type = models.ForeignKey(ItemType, primary_key=True, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)



