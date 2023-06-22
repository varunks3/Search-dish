# Generated by Django 4.2.2 on 2023-06-21 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('items', models.JSONField()),
                ('lat_long', models.CharField(max_length=255)),
                ('full_details', models.JSONField()),
            ],
        ),
    ]