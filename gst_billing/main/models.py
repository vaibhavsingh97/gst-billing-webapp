from django.db import models


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
