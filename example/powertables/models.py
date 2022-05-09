from django.db import models

from example.powertables.utils import get_model_fields


class PowerTableManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .order_by(*get_model_fields(self.model, option="name"))
        )


class PowerTableModel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    objects = PowerTableManager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    __repr__ = __str__
