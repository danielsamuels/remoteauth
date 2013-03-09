from django.http import HttpResponse
from .models import Rank
import json


def rank_listing(request):
    ranks = Rank.objects.filter(
        purchasable=True,
    )

    rank_obj = []

    for rank in ranks:
        rank_dict = {
            "name": rank.name,
            "price": str(rank.price) if rank.price > 0.0 else 'Free',
            "colour": rank.colour
        }

        rank_obj.append(rank_dict)

    return HttpResponse(json.dumps(rank_obj), content_type="application/json")


def rank_details(request, rank):
    # try:
    get_rank = Rank.objects.get(
        name__iexact=rank,
        purchasable=True,
    )

    rank = {
        "name": get_rank.name,
        "price": str(get_rank.price) if get_rank.price > 0.0 else 'Free',
        "colour": get_rank.colour,
        "description": [line.text for line in get_rank.descriptionline_set.all()]
    }
    # except:
        # rank = False

    return HttpResponse(json.dumps(rank), content_type="application/json")
