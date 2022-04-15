from django.forms import modelform_factory
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from .models import Contact
from .utils import get_model_fields


class PowerTableView(FormMixin, ListView):
    model = None
    paginate_by = 50

    def get_form_class(self):
        model_form_meta = modelform_factory(
            self.model, fields=get_model_fields(self.model, option="name")
        )
        return model_form_meta

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
            for field in get_model_fields(self.model)
            if [item for item in form.data.getlist(field.name) if item]
        }
        fields = get_model_fields(self.model, option="name")
        return queryset.filter(**kwargs).order_by(*fields)


class ContactPowerTableView(PowerTableView):
    model = Contact
