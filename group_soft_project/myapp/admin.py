from django.contrib import admin

# Register your models here.
from .models import ItemType, AmountType

admin.site.register(ItemType)
admin.site.register(AmountType)