# Generated by Django 3.2.7 on 2022-04-21 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_vehicle_id_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='HovLane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'HovLane',
            },
        ),
        migrations.CreateModel(
            name='HovMilestone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('is_enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_HovLane', models.ForeignKey(db_column='id_HovLane', on_delete=django.db.models.deletion.CASCADE, to='core.hovlane')),
            ],
            options={
                'db_table': 'HovMilestone',
            },
        ),
    ]
