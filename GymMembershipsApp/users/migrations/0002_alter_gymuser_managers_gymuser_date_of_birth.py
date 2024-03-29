# Generated by Django 5.0.1 on 2024-03-10 19:47

import GymMembershipsApp.users.managers
import GymMembershipsApp.users.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='gymuser',
            managers=[
                ('objects', GymMembershipsApp.users.managers.GymUserManager()),
            ],
        ),
        migrations.AddField(
            model_name='gymuser',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now, validators=[GymMembershipsApp.users.validators.validate_age_12_and_above]),
            preserve_default=False,
        ),
    ]
