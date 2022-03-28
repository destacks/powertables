from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name

    __repr__ = __str__


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    __repr__ = __str__


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    __repr__ = __str__


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    __repr__ = __str__
