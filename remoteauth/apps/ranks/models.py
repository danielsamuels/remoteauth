from django.db import models


class Rank(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )

    description = models.CharField(
        max_length=200,
        default='',
        blank=True,
        null=True
    )

    colour = models.CharField(
        max_length=1,
        default='F',
        choices=(
            ('0', 'Black'),
            ('1', 'Navy'),
            ('2', 'Green'),
            ('3', 'Teal'),
            ('4', 'Maroon'),
            ('5', 'Purple'),
            ('6', 'Olive'),
            ('7', 'Silver'),
            ('8', 'Grey'),
            ('9', 'Blue'),
            ('A', 'Lime'),
            ('B', 'Aqua'),
            ('C', 'Red'),
            ('D', 'Magenta'),
            ('E', 'Yellow'),
            ('F', 'White'),
        ),
        help_text='See <a href="{url}" target="_blank">{url}</a> for the colours.'.format(
            url='http://www.fcraft.net/wiki/Colors'
        )
    )

    purchasable = models.BooleanField(
        default=True
    )

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ("price", "name",)
