from functools import lru_cache
from typing import List

from django.db.models import Q
from django.forms import modelform_factory
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from .utils import get_model_fields


class PowertableView(FormMixin, ListView):
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

    @lru_cache(maxsize=1)
    def get_field_value_list(self, field_name: str) -> List:
        form = self.get_form()
        return [item for item in form.data.getlist(field_name) if item]

    def get_queryset(self):
        queryset = super().get_queryset()
        fields = [
            {"field": field, "value_list": self.get_field_value_list(field.name)}
            for field in get_model_fields(self.model)
            if self.get_field_value_list(field.name)
        ]
        field_names = get_model_fields(self.model, option="name")
        query = None
        for field in fields:
            value_list = field["value_list"]
            field_item = field["field"]
            has_icontains = (
                True if "icontains" in field_item.class_lookups.keys() else False
            )
            subquery = None

            for value in value_list:
                if has_icontains:
                    kwarg = {f"{field_item.name}__icontains": value}
                else:
                    kwarg = {f"{field_item.column}": value}
                if subquery is None:
                    subquery = Q(**kwarg)
                else:
                    subquery.add(Q(**kwarg), Q.OR)

            if subquery is not None:
                if query is None:
                    query = subquery
                else:
                    query.add(subquery, Q.AND)

        # Sorting
        sorted_field_names = []
        for field_name in field_names:
            key = f"sorting_{field_name}"
            if key in self.request.GET.keys():
                if self.request.GET[key] == "asc":
                    sorted_field_names.append(field_name)
                else:
                    sorted_field_names.append(f"-{field_name}")
        if not sorted_field_names:
            sorted_field_names = field_names

        if query is None:
            return queryset.order_by(*sorted_field_names)
        else:
            return queryset.filter(query).order_by(*sorted_field_names)
