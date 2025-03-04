from django.core.cache import cache
from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date, datetime

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
        return {
            template_name: [
                {
                    **model_to_dict(obj),
                    "image_url": obj.image.url if obj.image else None,
                }
                for obj in objects
            ]
        }

    favorites = set(
        favorite_model.objects.filter(user=user).values_list(
            f"{model.__name__.lower()}_id", flat=True
        )
    )

    objects_with_favorites = [
        {
            **model_to_dict(obj),
            "is_favourite": obj.id in favorites,
            "image_url": (
                obj.image.url if obj.image else None
            ),  # Explicitly add image URL
        }
        for obj in objects
    ]

    return {template_name: objects_with_favorites}


def get_object_details(model, object_id, user, favorite_model):
    """Helper function to get object details including favorite status and adjacent IDs."""

    obj = get_object_or_404(model, pk=object_id)

    is_favorite = (
        favorite_model.objects.filter(
            **{f"{model.__name__.lower()}_id": obj.id}, user=user
        ).exists()
        if user.is_authenticated
        else False
    )

    prev_id = (
        model.objects.filter(id__lt=obj.id)
        .order_by("-id")
        .values_list("id", flat=True)
        .first()
    )
    next_id = (
        model.objects.filter(id__gt=obj.id)
        .order_by("id")
        .values_list("id", flat=True)
        .first()
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
        # Get destination details, favorite status, and adjacent IDs
        context, prev_id, next_id = get_object_details(
            Destination, id, request.user, FavouriteDestination
        )

        destination = context["destination"]
        trips = Trip.objects.filter(destination=destination)

        existing_bookings = {}
        if request.user.is_authenticated and trips:
            for trip in trips:
                booking = TripBooking.objects.filter(
                    user=request.user, trip=trip, start_date__gte=date.today()
                ).first()
                if booking:
                    existing_bookings[trip.id] = booking  # Store booking by trip ID

        context.update(
            {
                "prev_destination_id": prev_id,
                "next_destination_id": next_id,
                "trips": trips,
                "existing_bookings": existing_bookings,  # Pass as dictionary
            }
        )
        return render(request, "pages/destination.html", context)

    # Handle the list of destinations
    destinations_data = get_objects_with_favorites(
        Destination, FavouriteDestination, request.user, "destinations"
    )
    destinations_list = destinations_data["destinations"]  # Extract the list
    paginator = Paginator(destinations_list, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return render(request, "pages/destinations.html", context)


def hotels(request, id=None):
    if id:
        context, prev_id, next_id = get_object_details(
            Hotel, id, request.user, FavouriteHotel
        )
        context.update({"prev_hotel_id": prev_id, "next_hotel_id": next_id})
        return render(request, "pages/hotel.html", context)

    # Handle the list of destinations
    hotel_data = get_objects_with_favorites(
        Hotel, FavouriteHotel, request.user, "hotels"
    )
    hotel_list = hotel_data["hotels"]  # Extract the list
    paginator = Paginator(hotel_list, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return render(request, "pages/hotels.html", context)


def activities(request, id=None):
    if id:
        context, prev_id, next_id = get_object_details(
            Activity, id, request.user, FavouriteActivity
        )
        context.update({"prev_activity_id": prev_id, "next_activity_id": next_id})
        return render(request, "pages/activity.html", context)

    # Handle the list of destinations
    activity_data = get_objects_with_favorites(
        Activity, FavouriteActivity, request.user, "activities"
    )
    activity_list = activity_data["activities"]  # Extract the list
    paginator = Paginator(activity_list, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return render(request, "pages/activities.html", context)


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

    # Handle the list of destinations
    package_data = get_objects_with_favorites(
        Package, FavouritePackage, request.user, "packages"
    )
    package_list = package_data["packages"]  # Extract the list
    paginator = Paginator(package_list, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return render(request, "pages/packages.html", context)


@login_required(login_url="/login/")
def add_to_favourites(request):
    context_map = {
        "destination": (
            Destination,
            FavouriteDestination,
            "destination",
            "destinations_list",
        ),
        "trip": (Trip, FavouriteTrip, "trip", "trips_list"),
        "activity": (Activity, FavouriteActivity, "activity", "activities_list"),
        "package": (Package, FavouritePackage, "package", "packages_list"),
        "hotel": (Hotel, FavouriteHotel, "hotel", "hotels_list"),
    }

    obj_id = request.GET.get("id")
    context_type = request.GET.get("context")

    if not obj_id or not context_type or context_type not in context_map:
        return redirect("index")

    model, fav_model, obj_name, redirect_name = context_map[context_type]
    obj = get_object_or_404(model, pk=obj_id)
    fav_relation = fav_model.objects.filter(**{obj_name: obj}, user=request.user)

    if fav_relation.exists():
        fav_relation.delete()
    else:
        fav_model.objects.create(**{obj_name: obj}, user=request.user)

    return redirect(redirect_name)


@login_required(login_url="/login/")
def book_trip(request):
    if request.method == "POST":
        data = request.POST
        id = data["trip_id"][0]
        start_date = data["start_date"]

        if TripBooking.objects.filter(user=request.user, trip=id).exists():
            return redirect("total_booking")

        trip = get_object_or_404(Trip, pk=id)

        context = {"total": 0, "title": "", "subtitle": ""}
        context["title"] = trip.name
        context["subtitle"] = trip.destination
        context["total"] = trip.price

        cache.set(
            "booking",
            {"type": "trip", "data": trip, "start_date": start_date},
            timeout=60000,
        )

        return render(request, "pages/payments/payment.html", context=context)

    return render(request, "404.html")


@login_required(login_url="/login/")
def book_activity(request):
    if request.method == "POST":
        data = request.POST
        id = data["activity_id"][0]
        start_date = data["start_date"]

        if ActivityBooking.objects.filter(user=request.user, activity=id).exists():
            return redirect("total_booking")

        activity = get_object_or_404(Activity, pk=id)

        context = {"total": 0, "title": "", "subtitle": ""}
        context["title"] = activity.name
        context["subtitle"] = activity.description
        context["total"] = activity.price

        cache.set(
            "booking",
            {"type": "activity", "data": activity, "start_date": start_date},
            timeout=60000,
        )

        return render(request, "pages/payments/payment.html", context=context)

    return render(request, "404.html")


@login_required(login_url="/login/")
def book_package(request):
    if request.method == "POST":
        data = request.POST
        id = data["package_id"]
        start_date = data["start_date"]

        if PackageBooking.objects.filter(user=request.user, package=id).exists():
            return redirect("total_booking")

        package = get_object_or_404(Package, pk=id)

        context = {"total": 0, "title": "", "subtitle": ""}
        context["title"] = package.name
        context["subtitle"] = package.description
        context["total"] = package.price

        cache.set(
            "booking",
            {"type": "package", "data": package, "start_date": start_date},
            timeout=60000,
        )

        return render(request, "pages/payments/payment.html", context=context)

    return render(request, "404.html")


@login_required(login_url="/login/")
def book_hotel(request):
    if request.method == "POST":
        data = request.POST
        id = data["hotel_id"]
        start_date = data["start_date"]
        to_date = data["to_date"]

        if HotelBooking.objects.filter(user=request.user, hotel=id).exists():
            return redirect("total_booking")

        hotel = get_object_or_404(Hotel, pk=id)

        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(to_date, "%Y-%m-%d")
        total_days = (end - start).days
        total_price = hotel.price * total_days

        context = {"total": 0, "title": "", "subtitle": ""}
        context["title"] = hotel.name
        context["subtitle"] = hotel.description
        context["total"] = total_price

        cache.set(
            "booking",
            {
                "type": "hotel_homestay",
                "data": hotel,
                "start_date": start_date,
                "to_date": to_date,
            },
            timeout=60000,
        )

        return render(request, "pages/payments/payment.html", context=context)

    return render(request, "404.html")


@login_required(login_url="/login/")
def total_booking(request):
    from django.utils import timezone
    from django.db.models import CharField, Value
    from itertools import chain

    today = timezone.now().date()

    # Get all bookings with type annotations
    trip_bookings = TripBooking.objects.filter(user=request.user).annotate(
        booking_type=Value("trip", output_field=CharField())
    )
    activity_bookings = ActivityBooking.objects.filter(user=request.user).annotate(
        booking_type=Value("activity", output_field=CharField())
    )
    package_bookings = PackageBooking.objects.filter(user=request.user).annotate(
        booking_type=Value("package", output_field=CharField())
    )
    hotel_bookings = HotelBooking.objects.filter(user=request.user).annotate(
        booking_type=Value("hotel", output_field=CharField())
    )

    # Combine and split into upcoming/past bookings
    all_bookings = sorted(
        chain(trip_bookings, activity_bookings, package_bookings, hotel_bookings),
        key=lambda x: x.created_at,
        reverse=True,
    )

    upcoming_bookings = [b for b in all_bookings if b.start_date >= today]
    past_bookings = [b for b in all_bookings if b.start_date < today]

    return render(
        request,
        "pages/bookings.html",
        {
            "upcoming_bookings": upcoming_bookings,
            "past_bookings": past_bookings,
        },
    )


def booking_detail(request, id):
    return render(request, "pages/booking-detail.html")


def add_booking(user, transaction_id):
    cache_data = cache.get("booking")

    if cache_data:
        type_of_booking = cache_data.get("type")
        data = cache_data.get("data")
        start_date = cache_data.get("start_date")

        if type_of_booking == "trip":
            TripBooking.objects.create(
                trip=data,
                user=user,
                start_date=start_date,
                transaction_id=transaction_id,
            )
        elif type_of_booking == "activity":
            ActivityBooking.objects.create(
                activity=data,
                user=user,
                start_date=start_date,
                transaction_id=transaction_id,
            )
        elif type_of_booking == "package":
            PackageBooking.objects.create(
                package=data,
                user=user,
                start_date=start_date,
                transaction_id=transaction_id,
            )
        elif type_of_booking == "hotel_homestay":
            to_date = cache_data["to_date"]

            HotelBooking.objects.create(
                hotel=data,
                user=user,
                to_date=to_date,
                start_date=start_date,
                transaction_id=transaction_id,
            )
