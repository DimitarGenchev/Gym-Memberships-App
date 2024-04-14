# Generated by Django 5.0.1 on 2024-04-14 20:18

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_product_product_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='start_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2024, 4, 14))]),
        ),
    ]
