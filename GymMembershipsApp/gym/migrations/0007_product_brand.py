# Generated by Django 5.0.1 on 2024-02-18 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0006_brand_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gym.brand'),
            preserve_default=False,
        ),
    ]
