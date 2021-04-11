from django.db import models
from django.utils.translation import gettext as _

class Sighting(models.Model):
    Latitude = models.FloatField(
        help_text = _('Latitude'),)

    Longitude  = models.FloatField(
        help_text = _('Longitude'),)

    Unique_Squirrel_Id = models.CharField(
        max_length=80,
        help_text=_('The unique squirrel ID'),)

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = [
        (AM,_('AM')),
        (PM,_('PM')),
    ]

    Shift = models.CharField(
        max_length=2,
        help_text = _('AM or PM?'),
        choices=SHIFT_CHOICES,
        )


    Date = models.DateField(
        help_text = _('what is the date'),
        blank=True,
        )


    ADULT = 'ADULT'
    JUVENILE = 'JUVENILE'
    UNKNOWN = 'UNKNOWN'
    AGE_CHOICES = [
        (ADULT, _('ADULT')),
        (JUVENILE,_('JUVENILE')),
        (UNKNOWN, _('?'))
        ]
    Age = models.CharField(
        max_length=80,
        help_text= _('Age'),
        choices=AGE_CHOICES,
        blank=True,
        )


    Gray = 'Gray'
    Black = 'Black'
    Cinnamon = 'Cinnamon'

    COLOR_CHOICE=[
        (Gray, _('Gray')),
        (Black, _('Black')),
        (Cinnamon, _('Cinnamon')),
        ]

    Primary_Fur_Color = models.CharField(
        max_length=10,
        help_text = _('what is the fur color'),
        choices = COLOR_CHOICE,
        blank=True,
        )

    ABOVE_GROUND = 'Above Ground'
    GROUND_PLANE = 'Ground Plane'
    LOCATION_CHOICES = [
        (GROUND_PLANE, _('Ground Plane')),
        (ABOVE_GROUND, _('Above Ground')),
        ]
    Location =  models.CharField(
        max_length=80,
        choices = LOCATION_CHOICES,
        help_text = _('Location'),
        blank=True,
        )

    Specific_Location = models.CharField(
        max_length=80,
        help_text=_('specific location'),
        blank=True,
        )

    Running = models.BooleanField(
        help_text=_('Running'),
        blank=True
        )
    
    Chasing = models.BooleanField(
        help_text=_('Chasing'),
        blank=True
        )

    Climbing = models.BooleanField(
        help_text=_('Climbing'),
        blank=True
        )

    Eating = models.BooleanField(
        help_text = _('Eating'),
        blank=True,
        )

    Foraging = models.BooleanField(
        help_text = _('Foraging'),
        blank=True,
        )

    Other_Activities = models.CharField(
        help_text = _('Other Activities'),
        max_length = 80,
        blank = True
        )

    Kuks = models.BooleanField(
        help_text = _('Kuks'),
        blank=True,
        )

    Quaas = models.BooleanField(
        help_text = _('Quaas'),
        blank=True,
    )

    Moans = models.BooleanField(
        help_text = _('Moans'),
        blank=True,
    )

    Tail_Flags = models.BooleanField(
        help_text = _('Tail_Flags'),
        blank=True,
    )

    Tail_Twitches = models.BooleanField(
        help_text = _('Tail_Twitches'),
        blank=True,
    )

    Approaches = models.BooleanField(
        help_text = _('Approaches'),
        blank=True,
    )

    Indifferent = models.BooleanField(
        help_text = _('Indifferent'),
        blank=True,
    )

    Runs_From = models.BooleanField(
        help_text = _('Runs_From'),
        blank=True,
    )



