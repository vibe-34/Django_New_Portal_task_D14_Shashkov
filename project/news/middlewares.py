# Diese Datei (middlewares.py) wird ben?tigt, um die Zeitzonenbehandlung zu implementieren.

import pytz
from django.utils import timezone


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get('django_timezone')  # Ich versuche, die Zeitzone aus der Sitzung zu ermitteln
        #  Wenn es sich um eine Sitzung handelt, legen wir eine solche Zeitzone fest.
        #  Wenn es nicht vorhanden ist, ist es nicht installiert und die Zeitzone
        #  muss standardm??ig eingestellt sein (Serverzeit).
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)
