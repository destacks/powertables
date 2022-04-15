from django.contrib import admin

from .models import Company, Contact, Position


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass
