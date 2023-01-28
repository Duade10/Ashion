from django.db import models
from core.models import AbstractTimeStampedModel
from shortuuidfield import ShortUUIDField


class Vendor(AbstractTimeStampedModel):
    uuid = ShortUUIDField()
    user = models.OneToOneField("users.User", related_name="vendor", on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255)
    contact_mail = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.store_name
