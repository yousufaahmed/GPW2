from django import forms
from .models import ItemType, IndividualItems

class AddToInventoryForm(forms.ModelForm):
    type = forms.ModelChoiceField(
        queryset=ItemType.objects.all(), 
        empty_label="Select Item Type",
        to_field_name="unique_barcode",  # Value should be barcode
        label="Item Type"
    )
    expiration_date = forms.DateField(widget=forms.SelectDateWidget)
    
    class Meta:
        model = IndividualItems
        fields = ['type', 'expiration_date', 'amount']
