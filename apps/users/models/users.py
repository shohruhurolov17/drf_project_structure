from apps.shared.models import AbstractBaseModel
from apps.shared.utils import generate_base64
from django.db import models


class CustomUser(AbstractBaseModel):

    id = models.CharField(
        primary_key=True,
        unique=True,
        max_length=22,
        editable=False,
        default=generate_base64
    )

    class Meta:

        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering  = ['-created_time']