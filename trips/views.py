from django.shortcuts import redirect, render

from .models import (
    Destination,
    Trip,
    Activities,
    Package,
    Hotel,
    FavouriteDestination,
    FavouriteTrip,
    FavouriteActivity,
    FavouritePackage,
    FavouriteHotel,
)


# Create your views here.
def index(request):
    trips = {}

    searchParam = request.GET.get("q", "default")

    if searchParam != "default":
        trips = searchParam
    else:
        trips = ""

    return render(request, "pages/explore.html", {"trips": trips})


def destinations(request, id=None):
    if id is not None:
        destination = Destination.objects.get(pk=id)
        is_favourite = FavouriteDestination.objects.filter(
            destination=destination, user=request.user
        ).exists()
        return render(
            request,
            "pages/destination.html",
            {"destination": destination, "is_favourite": is_favourite},
        )

    destinations = Destination.objects.all()
    favourites = FavouriteDestination.objects.filter(user=request.user).values_list(
        "destination_id", flat=True
    )
    destinations_with_favourites = [
        {**destination.__dict__, "is_favourite": destination.id in favourites}
        for destination in destinations
    ]

    return render(
        request,
        "pages/destinations.html",
        {"destinations": destinations_with_favourites},
    )


def hotels(request, id=None):
    if id is not None:
        hotel = Hotel.objects.get(pk=id)
        is_favourite = FavouriteHotel.objects.filter(
            hotel=hotel, user=request.user
        ).exists()
        return render(
            request,
            "pages/hotel.html",
            {"hotel": hotel, "is_favourite": is_favourite},
        )

    hotels = Hotel.objects.all()
    favourites = FavouriteHotel.objects.filter(user=request.user).values_list(
        "hotel_id", flat=True
    )
    hotels_with_favourites = [
        {**hotel.__dict__, "is_favourite": hotel.id in favourites} for hotel in hotels
    ]

    return render(
        request,
        "pages/hotels.html",
        {"hotels": hotels_with_favourites},
    )


def activities(request, id=None):
    if id is not None:
        activity = Activities.objects.get(pk=id)
        is_favourite = FavouriteActivity.objects.filter(
            activity=activity, user=request.user
        ).exists()
        return render(
            request,
            "pages/activity.html",
            {"activity": activity, "is_favourite": is_favourite},
        )

    activities = Activities.objects.all()
    favourites = FavouriteActivity.objects.filter(user=request.user).values_list(
        "activity_id", flat=True
    )
    activities_with_favourites = [
        {**activity.__dict__, "is_favourite": activity.id in favourites}
        for activity in activities
    ]

    return render(
        request,
        "pages/activities.html",
        {"activities": activities_with_favourites},
    )

def packages(request, id=None):
    if id is not None:
        package = Package.objects.get(pk=id)
        is_favourite = FavouritePackage.objects.filter(
            package=package, user=request.user
        ).exists()
        return render(
            request,
            "pages/package.html",
            {"package": package, "is_favourite": is_favourite},
        )

    packages = Package.objects.all()
    favourites = FavouritePackage.objects.filter(user=request.user).values_list(
        "package_id", flat=True
    )
    packages_with_favourites = [
        {**package.__dict__, "is_favourite": package.id in favourites}
        for package in packages
    ]

    return render(
        request,
        "pages/packages.html",
        {"packages": packages_with_favourites},
    )


def add_to_favourites(request):
    if not request.user.is_authenticated:
        return redirect("login")

    id = request.GET.get("id")
    context = request.GET.get("context")
    
    if context == "destination":
        if FavouriteDestination.objects.filter(
            destination=Destination.objects.get(pk=id), user=request.user
        ).exists():
            FavouriteDestination.objects.filter(
                destination=Destination.objects.get(pk=id), user=request.user
            ).delete()
        else:
            fav_destination = FavouriteDestination()
            fav_destination.user = request.user
            fav_destination.destination = Destination.objects.get(pk=id)
            fav_destination.save()
    elif context == "trip":
        if FavouriteTrip.objects.filter(
            trip=Trip.objects.get(pk=id), user=request.user
        ).exists():
            FavouriteTrip.objects.filter(
                trip=Trip.objects.get(pk=id), user=request.user
            ).delete()
        else:
            fav_trip = FavouriteTrip()
            fav_trip.user = request.user
            fav_trip.trip = Trip.objects.get(pk=id)
            fav_trip.save()
    elif context == "activity":
        if FavouriteActivity.objects.filter(
            activity=Activities.objects.get(pk=id), user=request.user
        ).exists():
            FavouriteActivity.objects.filter(
                activity=Activities.objects.get(pk=id), user=request.user
            ).delete()
        else:
            fav_activity = FavouriteActivity()
            fav_activity.user = request.user
            fav_activity.activity = Activities.objects.get(pk=id)
            fav_activity.save()
    elif context == "package":
        if FavouritePackage.objects.filter(
            package=Package.objects.get(pk=id), user=request.user
        ).exists():
            FavouritePackage.objects.filter(
                package=Package.objects.get(pk=id), user=request.user
            ).delete()
        else:
            fav_package = FavouritePackage()
            fav_package.user = request.user
            fav_package.package = Package.objects.get(pk=id)
            fav_package.save()
    elif context == "hotel":
        if FavouriteHotel.objects.filter(
            hotel=Hotel.objects.get(pk=id), user=request.user
        ).exists():
            FavouriteHotel.objects.filter(
                hotel=Hotel.objects.get(pk=id), user=request.user
            ).delete()
        else:
            fav_hotel = FavouriteHotel()
            fav_hotel.user = request.user
            fav_hotel.hotel = Hotel.objects.get(pk=id)
            fav_hotel.save()

    return redirect("destination", id=id)
