from django.db import models
from django.forms import modelform_factory
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from .models import Contact


class PowerTableView(FormMixin, ListView):
    model = None
    paginate_by = 50

    @staticmethod
    def get_model_fields(model: models.Model):
        return [field for field in model._meta.get_fields() if field.column != "id"]

    def get_form_class(self):
        return modelform_factory(
            self.model, fields=[f.name for f in self.get_model_fields(self.model)]
        )

    def get_form_kwargs(self):
        kwargs = {
            "initial": self.get_initial(),
            "prefix": self.get_prefix(),
        }
        if self.request.method == "GET":
            kwargs.update({"data": self.request.GET})
        return kwargs

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.get_form()
        kwargs = {
            f"{field.column}__in": [
                item for item in form.data.getlist(field.name) if item
            ]
            for field in self.get_model_fields(self.model)
            if [item for item in form.data.getlist(field.name) if item]
        }
        return queryset.filter(**kwargs)


class ContactPowerTableView(PowerTableView):
    model = Contact
