from django import forms
from main.models import AddNewItemModel


class AddNewItemForm(forms.ModelForm):
    class Meta:
        model = AddNewItemModel
        fields = ('id', 'name', 'quantity', 'price_per_unit', 'gst')

    def clean(self):
        cleaned_data = super().clean()
        id = cleaned_data.get("id")
        quantity = cleaned_data.get("quantity")
        price_per_unit = cleaned_data.get("price_per_unit")
        if id < 1:
            raise forms.ValidationError(
                "Id can't be less than 0"
            )
        if quantity < 1:
            raise forms.ValidationError(
                "Quantity can't be zero"
            )
        elif price_per_unit < 1:
            raise forms.ValidationError(
                "Price can't be zero"
            )
