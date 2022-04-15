from typing import List

from django.db import models


def get_model_fields(model: models.Model, option: str = "all") -> List:
    allowed_options = ["all", "name", "column"]
    forbidden_fields = ["id"]
    message = f'Parameter "option" with value "{option}" must be in {allowed_options}'
    fields = [
        field for field in model._meta.fields if field.name not in forbidden_fields
    ]

    if option == "all":
        return fields
    elif option == "name":
        return [field.name for field in fields]
    elif option == "column":
        return [field.column for field in fields]
    else:
        raise ValueError(message)
