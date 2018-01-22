from django.contrib import admin
from main.models import AddNewItemModel

class AddNewItem(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'price_per_unit', 'gst', 'created_at')
    class Meta:
        model = AddNewItemModel

admin.site.register(AddNewItemModel, AddNewItem)
