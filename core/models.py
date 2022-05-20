from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Vehicle(models.Model):

    # ID: an id is automatically gereated by django
    # on_delete: behaviour to adopt when the referenced object is deleted
    # explicitly specify column's name using db_column, else Django appends '_id'
    id_user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, db_column='id_user')
    # TODO validate with regex and Raise a ValidationError
    plate_number = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)  # TODO: limitar las "choices

    # MaxValueValidator Raises a ValidationError with a code of 'max_value' if value is greater than limit_value
    seats = models.PositiveSmallIntegerField(default=1, validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])
    is_enabled = models.BooleanField(default=True)

    class Meta:
        # rename DB table
        # by default django names it [app_name]_[model_name], which would be "core_vehicle"
        db_table = 'vehicle'


class HovLane(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    is_enabled = models.BooleanField(default=False, verbose_name="Habilitado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Actualizado")

    class Meta:
        db_table = 'hov_lane'
        verbose_name = 'Carril HOV'
        verbose_name_plural = 'Carriles HOV'

    def __str__(self):
        return self.name


class HovMilestone(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    id_HovLane = models.ForeignKey(
        "HovLane", on_delete=models.CASCADE, db_column='id_HovLane', verbose_name="Carril HOV")
    location = models.CharField(max_length=200, verbose_name="Localización")

    is_enabled = models.BooleanField(default=True, verbose_name="Habilitado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Actualizado")

    class Meta:
        db_table = 'hov_milestone'
        verbose_name = 'Milestone HOV'
        verbose_name_plural = 'Milestones HOV'

    def __str__(self):
        return self.name
