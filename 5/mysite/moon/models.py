from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def NatureNumbersValidator(value):
    if value<0:
        raise ValidationError(
            _("%(value)s is not a natural number"),
            params={'value': value}
        )
        
class NewModel(models.Model):
    countNumber = models.IntegerField(validators=[NatureNumbersValidator])
