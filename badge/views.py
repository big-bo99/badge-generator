from django.shortcuts import render
import anybadge

from django.http import HttpResponse
from PIL import Image

import random
#INK = "red", "green", "yellow"
#INK = "red"

def index(request, value):
    v = int(value)
    anybadge(v)
    print(value)
    if (v > 1) & (v < 33):
        INK = "red"
    elif (v > 33) & (v < 66):
        INK = "yellow"
    elif (v > 66) & (v < 100):
        INK = "green"


    # ... create/load image here ...
    image = Image.new("RGB", (200, 50), INK)

    # serialize to HTTP response
    response = HttpResponse(content_type="image/png")
    #response = HttpResponse(json.dumps("image/png"), content_type='application/json')
    image.save(response, "PNG")

    return response

def anybadge(v):
    import anybadge
    if (v > 1) & (v < 33):
        d = "critical issues"
    elif (v > 33) & (v < 66):
        d = "minor issues"
    elif (v > 66) & (v < 100):
        d = "passed"

    thresholds = {"critical issues": 'red',
          "minor issues": 'yellow',
          "passed": 'green',
          }

    badge = anybadge.Badge('Mythril-Scanner:', d, thresholds=thresholds)

    badge.write_badge('badge/media/badges/{}pylint.svg'.format(v))
