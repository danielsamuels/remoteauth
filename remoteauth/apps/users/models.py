from django.db import models

class User(models.Model):

    username = models.CharField(
        "minecraft username",
        max_length=100,
    )

    rank = models.ForeignKey(
        'ranks.Rank',
    )
