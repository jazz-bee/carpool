# Generated by Django 3.2.7 on 2022-04-20 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_vehicle_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='id_user',
            field=models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
