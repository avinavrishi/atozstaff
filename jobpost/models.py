from django.db import models
from django_editorjs_fields import EditorJsJSONField
from django.contrib.auth import get_user_model
from mysite.models import service


# Create your models here.


class jobPost(models.Model):
    title = models.CharField("Title", max_length=20)
    type = models.CharField("Type", max_length=20)
    role = models.CharField("Role", max_length=20)
    # location
    experience_min = models.IntegerField()
    experience_max = models.IntegerField()
    premium = models.BooleanField(default=False)
    description = EditorJsJSONField()
    category = models.TextField()  # add choice
    salary_lower_range = models.TextField()
    salary_upper_range = models.TextField()
    postedby = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateField("Date Posted", auto_now_add=True)
    modified = models.DateField("Date Modified", auto_now=False)


class service_requirement(models.Model):
    service_type = models.ForeignKey(service, on_delete=models.CASCADE)
    service_description = models.TextField("Service Description")
    created = models.DateField("Date Created", auto_now_add=False)
    phone_number = models.IntegerField("Phone Number")
