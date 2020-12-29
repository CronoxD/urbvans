
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class EconomicNumberHistory(models.Model):
    """Economic Number history to have a control about the secuence generations"""

    # The economic number fisrt part, a field to searching
    economic_number_initial = models.CharField(
        _('Initial number initial'),
        max_length=50
    )

    # Secuence number
    number = models.IntegerField(
        _('Number secuence')
    )

    economic_number = models.CharField(
        _('Economic number'),
        max_length=100
    )
