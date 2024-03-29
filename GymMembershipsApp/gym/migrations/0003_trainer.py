# Generated by Django 5.0.1 on 2024-03-13 18:57

import GymMembershipsApp.users.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2), GymMembershipsApp.users.validators.validate_name_contains_alphabet_only])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2), GymMembershipsApp.users.validators.validate_name_contains_alphabet_only])),
                ('description', models.TextField()),
                ('trainer_type', models.CharField(choices=[('bodybuilding', 'Bodybuilding'), ('strength training', 'Strength training'), ('calisthenics', 'Calisthenics'), ('cardio', 'Cardio'), ('crossfit', 'Crossfit')], max_length=20)),
                ('trainer_picture', models.ImageField(upload_to='trainer_pictures')),
            ],
        ),
    ]
