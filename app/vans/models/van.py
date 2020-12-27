
# Django
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

# Utilities
import uuid as _uuid


class Van(models.Model):
    """Van model"""
    uuid = models.UUIDField(
        primary_key=True,
        default=_uuid.uuid4,
        editable=False
    )

    plates = models.CharField(
        _('Plates'),
        max_length=100,
        unique=True,
        validators=[
            RegexValidator(
                regex='^([A-Za-z]|[0-9]){3}-[0-9]{3}$',
                message=_('The plates dont have the correct format'),
                code='invalid_plates',
            )
        ]
    )

    economic_number = models.CharField(
        _('Economic number'),
        max_length=100,
        unique=True
    )

    seats = models.IntegerField(
        _('Seats'),
    )

    status = models.CharField(
        _('Status'),
        max_length=70,
        choices=[
            ('ACTIVE', 'Activa'),
            ('REPAIR', 'En reparación'),
        ]
    )

    created_at = models.DateTimeField(
        _('Created at'),
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        _('Udpated at'),
        auto_now=True
    )


@receiver(post_save, sender=Van)
def economic_number_handle(sender, created, instance, **kwargs):
    """Generate the economic number secuence"""
    if created:
        last_van = sender.objects.filter(
            economic_number__startswith=instance.economic_number,
        ).exclude(
            uuid=instance.uuid
        ).order_by('-economic_number').first()

        if last_van:
            number = last_van.economic_number.split('-')[1]
            number = int(number) + 1

            instance.economic_number = f'{instance.economic_number}-{str(number).zfill(4)}'
            instance.save()
        else:
            instance.economic_number = f'{instance.economic_number}-0001'
            instance.save()
