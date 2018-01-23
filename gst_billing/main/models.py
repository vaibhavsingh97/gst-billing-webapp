from django.db import models
from django.utils.crypto import get_random_string

class AddNewItemModel(models.Model):
    GST_PERCENTAGE = (
        ('5', '5%'),
        ('12', '12%'),
        ('18', '18%'),
        ('28', '28%'),
    )
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=10)
    quantity = models.IntegerField()
    price_per_unit = models.IntegerField()
    gst = models.CharField(max_length=5, choices=GST_PERCENTAGE, default='5')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(AddNewItemModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# class CreateBill(models.Model):
#     id =  models.IntegerField(get_random_string(length=6), auto_created=True, primary_key=True,)
#     item_name = models.CharField(max_length=10)
#     Bill_quantity = models.IntegerField()
#     amount = AddNewItemModel.price_per_unit * Bill_quantity
#     tax = amount * (AddNewItemModel.gst /100)
#     total_amount = amount + tax
#
#     def save(self, *args, **kwargs):
#         super(CreateBill, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.id