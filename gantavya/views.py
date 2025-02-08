from django.shortcuts import render

from trips.models import Destination, Trip


def index(request):
    trips = Trip.objects.all()[:6]
    destination = Destination.objects.all()[:6]

    return render(request, "index.html", {"trips": trips, "destinations": destination})


def about(request):
    return render(request, "pages/about.html")


def after_federated_signup(request):
    return render(request, "pages/after_federate_signup.html")
