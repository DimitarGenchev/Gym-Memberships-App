from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from GymMembershipsApp.users.utils import calculate_age


def validate_age_12_and_above(date_of_birth):
    age = calculate_age(date_of_birth)

    if age < 12:
        raise ValidationError(
            _('You must be at least 12 years old to register.'),
            params={'value': date_of_birth},
        )


def validate_name_contains_alphabet_only(value):
    if not value.isalpha():
        raise ValidationError(
            _('First and last names should only contain alphabetic characters.'),
            params={'value': value},
        )
