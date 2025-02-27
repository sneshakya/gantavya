from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date

from .models import (
    ActivityBooking,
    Destination,
    HotelBooking,
    PackageBooking,
    Trip,
    Activity,
    Package,
    Hotel,
    FavouriteDestination,
    FavouriteTrip,
    FavouriteActivity,
    FavouritePackage,
    FavouriteHotel,
    TripBooking,
)


def get_objects_with_favorites(model, favorite_model, user, template_name):
    """Helper function to get objects with favorite status for authenticated users."""

    objects = model.objects.all()
    if not user.is_authenticated:
        return {template_name: objects}

    favorites = favorite_model.objects.filter(user=user).values_list(
        f"{model.__name__.lower()}_id", flat=True
    )
    objects_with_favorites = [
        {**obj.__dict__, "is_favourite": obj.id in favorites} for obj in objects
    ]
    return {template_name: objects_with_favorites}


def get_object_details(model, object_id, user, favorite_model):
    """Helper function to get object details including favorite status and adjacent IDs."""

    obj = get_object_or_404(model, pk=object_id)
    is_favorite = (
        favorite_model.objects.filter(
            **{model.__name__.lower(): obj}, user=user
        ).exists()
        if user.is_authenticated
        else False
    )

    object_ids = list(model.objects.order_by("id").values_list("id", flat=True))
    current_index = object_ids.index(object_id)
    prev_id = object_ids[current_index - 1] if current_index > 0 else None
    next_id = (
        object_ids[current_index + 1] if current_index < len(object_ids) - 1 else None
    )

    return {model.__name__.lower(): obj, "is_favourite": is_favorite}, prev_id, next_id


def index(request):
    search_query = request.GET.get("q", "")
    trips = (
        Trip.objects.filter(name__icontains=search_query)
        if search_query
        else Trip.objects.all()
    )
    return render(request, "pages/explore.html", {"trips": trips})


def destinations(request, id=None):
    if id:
        context, prev_id, next_id = get_object_details(
            Destination, id, request.user, FavouriteDestination
        )
        destination = context["destination"]
        trip = Trip.objects.filter(destination=destination)
        trip_price = trip.values_list("price", flat=True).first()

        existing_booking = None
        if request.user.is_authenticated:
            # Check for active bookings that haven't started yet
            active_bookings = TripBooking.objects.filter(
                user=request.user, trip=trip.first(), start_date__gte=date.today()
            )
            existing_booking = active_bookings.first()

        context.update(
            {
                "prev_destination_id": prev_id,
                "next_destination_id": next_id,
                "trip": trip.first(),
                "existing_booking": existing_booking,
            }
        )
        return render(request, "pages/destination.html", context)
    return render(
        request,
        "pages/destinations.html",
        get_objects_with_favorites(
            Destination, FavouriteDestination, request.user, "destinations"
        ),
    )


def hotels(request, id=None):
    if id:
        context, prev_id, next_id = get_object_details(
            Hotel, id, request.user, FavouriteHotel
        )
        context.update({"prev_hotel_id": prev_id, "next_hotel_id": next_id})
        return render(request, "pages/hotel.html", context)
    return render(
        request,
        "pages/hotels.html",
        get_objects_with_favorites(Hotel, FavouriteHotel, request.user, "hotels"),
    )


def activities(request, id=None):
    if id:
        context, prev_id, next_id = get_object_details(
            Activity, id, request.user, FavouriteActivity
        )
        context.update({"prev_activity_id": prev_id, "next_activity_id": next_id})
        return render(request, "pages/activity.html", context)
    return render(
        request,
        "pages/activities.html",
        get_objects_with_favorites(
            Activity, FavouriteActivity, request.user, "activities"
        ),
    )


def packages(request, id=None):
    if id:
        context, prev_id, next_id = get_object_details(
            Package, id, request.user, FavouritePackage
        )
        package = Package.objects.get(id=id)
        existing_booking = (
            PackageBooking.objects.filter(user=request.user, package=package.id).first()
            if request.user.is_authenticated
            else None
        )

        context.update(
            {
                "prev_package_id": prev_id,
                "next_package_id": next_id,
                "existing_booking": existing_booking,
            }
        )
        return render(request, "pages/package.html", context)
    return render(
        request,
        "pages/packages.html",
        get_objects_with_favorites(Package, FavouritePackage, request.user, "packages"),
    )


@login_required(login_url="/login/")
def add_to_favourites(request):
    context_map = {
        "destination": (Destination, FavouriteDestination, "destination"),
        "trip": (Trip, FavouriteTrip, "trip"),
        "activity": (Activity, FavouriteActivity, "activity"),
        "package": (Package, FavouritePackage, "package"),
        "hotel": (Hotel, FavouriteHotel, "hotel"),
    }

    obj_id = request.GET.get("id")
    context_type = request.GET.get("context")

    if not obj_id or not context_type or context_type not in context_map:
        return redirect("index")

    model, fav_model, redirect_name = context_map[context_type]
    obj = get_object_or_404(model, pk=obj_id)
    fav_relation = fav_model.objects.filter(**{redirect_name: obj}, user=request.user)

    if fav_relation.exists():
        fav_relation.delete()
    else:
        fav_model.objects.create(**{redirect_name: obj}, user=request.user)

    return redirect(redirect_name, id=obj_id)


@login_required(login_url="/login/")
def book_trip(request, id):
    if TripBooking.objects.filter(user=request.user, trip=id).exists():
        return redirect("bookings")

    context = {"total": 0, "title": "", "subtitle": ""}
    trip = get_object_or_404(Trip, pk=id)

    context["title"] = trip.destination.name
    context["subtitle"] = trip.destination.description
    context["total"] = trip.price

    return render(request, "pages/payments/payment.html", context=context)
    trip_booking = TripBooking.objects.create(trip=trip, user=request.user)
    return redirect("bookings")


@login_required(login_url="/login/")
def book_activity(request, id):
    if ActivityBooking.objects.filter(user=request.user, activity=id).exists():
        return redirect("bookings")

    activity = get_object_or_404(Activity, pk=id)
    activity_booking = ActivityBooking.objects.create(
        activity=activity, user=request.user
    )
    return redirect("bookings")


@login_required(login_url="/login/")
def book_package(request, id):
    if PackageBooking.objects.filter(user=request.user, package=id).exists():
        return redirect("bookings")

    package = get_object_or_404(Package, pk=id)
    package_booking = PackageBooking.objects.create(package=package, user=request.user)
    return redirect("bookings")


@login_required(login_url="/login/")
def bookings(request):
    from django.utils import timezone
    from itertools import chain

    today = timezone.now().date()

    # Get all bookings across different types
    trip_bookings = TripBooking.objects.filter(user=request.user)
    activity_bookings = ActivityBooking.objects.filter(user=request.user)
    package_bookings = PackageBooking.objects.filter(user=request.user)
    hotel_bookings = HotelBooking.objects.filter(user=request.user)

    # Combine and split into upcoming/past bookings
    all_bookings = list(
        chain(trip_bookings, activity_bookings, package_bookings, hotel_bookings)
    )
    upcoming_bookings = [b for b in all_bookings if b.created_at >= today]
    past_bookings = [b for b in all_bookings if b.created_at < today]

    return render(
        request,
        "pages/bookings.html",
        {
            "upcoming_bookings": sorted(upcoming_bookings, key=lambda x: x.created_at),
            "past_bookings": sorted(
                past_bookings, key=lambda x: x.created_at, reverse=True
            ),
        },
    )
