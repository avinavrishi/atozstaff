from django.db import models


# Create your models here.
class service(models.Model):
    title = models.CharField("Title", max_length=20)
    image = models.ImageField(
        "Serice Icon",
        upload_to="services/icons/",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
    )
    code = models.CharField("service code", max_length=5)
    description = models.TextField("Description")
    order_by = models.IntegerField("Order By", unique=True)
