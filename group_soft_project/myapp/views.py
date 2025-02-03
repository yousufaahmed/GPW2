
# Create your views here.
from django.shortcuts import render, redirect
from .models import IndividualItems, ItemType
from .forms import AddToInventoryForm

def add_to_inventory(request):

    item_types = ItemType.objects.all()

    if request.method == "POST":
        form = AddToInventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/addToInventory')  # Redirect after successful submission
    else:
        form = AddToInventoryForm()
    
    return render(request, "add_to_inventory.html", {"form": form,  "item_types": item_types})
