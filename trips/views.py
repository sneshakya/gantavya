from django.shortcuts import render

from . import models


# Create your views here.
def index( request ):
	trips = { }

	searchParam = request.GET.get( 'q', 'default' )

	if searchParam != "default":
		trips = searchParam
	else:
		trips = ""

	return render(
		request,
		"pages/explore.html",
		{ "trips": trips }
	)


def destinations( request, id=None ):
	if id is not None:
		return render(
			request,
			"pages/destination.html",
			{
				"destination": models.Destination.objects.get( pk=id )
			}
		)

	destinations = models.Destination.objects.all()

	return render(
		request,
		"pages/destinations.html",
		{
			"destinations": destinations
		}
	)
