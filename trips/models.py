from email.policy import default
from uuid import uuid1
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import CustomUser
from payments.models import PaymentHistory


class BaseModel(models.Model):
    """Abstract base model with common fields"""

    product_code = models.CharField(
        _("product code"), default=uuid1(), editable=False, max_length=100
    )

    created_at = models.DateField(_("created at"), auto_now_add=True)
    updated_at = models.DateField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True


class FavouriteBaseModel(BaseModel):
    """Abstract model for favorite relationships"""

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="%(class)ss"
    )

    class Meta:
        abstract = True


class ReviewBaseModel(BaseModel):
    """Abstract model for reviews"""

    comment = models.TextField(_("comment"))
    rating = models.IntegerField(
        _("rating"), validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        abstract = True
        ordering = ("-created_at",)


class BookingBaseModel(BaseModel):
    """Abstract model for bookings"""

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="%(class)ss"
    )
    start_date = models.DateField(_("start date"))
    transaction_id = models.ForeignKey(
        PaymentHistory, on_delete=models.CASCADE, null=True, blank=True
    )

    def get_booking_type():
        return ""

    class Meta:
        abstract = True
        ordering = ("-start_date",)


class Destination(models.Model):
    name = models.CharField(_("name"), max_length=100)
    description = models.TextField(_("description"), blank=True)
    image = models.ImageField(
        _("image"),
        upload_to="images/destination/",
        default="images/destination/default.jpg",
    )
    longitude = models.DecimalField(_("longitude"), max_digits=10, decimal_places=6)
    latitude = models.DecimalField(_("latitude"), max_digits=10, decimal_places=6)
    city = models.CharField(_("city"), max_length=100)
    location = models.CharField(_("location"), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("destination")
        verbose_name_plural = _("destinations")


class Trip(models.Model):
    name = models.CharField(_("trip name"), default="trip", max_length=50)
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name="trips"
    )
    image = models.ImageField(
        _("image"), upload_to="images/trip/", default="images/trip/default.jpg"
    )
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    description = models.CharField(
        _("trip description"), default="Description", max_length=500
    )
    travelling_days = models.IntegerField(_("travelling days"), default=0)

    def __str__(self):
        return f"{self.destination.name} Trip"

    class Meta:
        verbose_name = _("trip")
        verbose_name_plural = _("trips")


class Activity(BaseModel):
    name = models.CharField(_("name"), max_length=100)
    description = models.TextField(_("description"), blank=True)
    image = models.ImageField(
        _("image"),
        upload_to="images/activities/",
        default="images/activities/default.jpg",
    )
    location = models.CharField(_("location"), max_length=100)
    city = models.CharField(_("city"), max_length=100)
    price = models.FloatField(default=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("activity")
        verbose_name_plural = _("activities")
        ordering = ("-created_at",)


class Package(BaseModel):
    name = models.CharField(_("name"), max_length=100)
    description = models.TextField(_("description"), blank=True)
    image = models.ImageField(
        _("image"), upload_to="images/package/", default="images/package/default.jpg"
    )
    location = models.CharField(_("location"), max_length=100)
    price = models.DecimalField(_("price"), max_digits=20, decimal_places=2)
    duration = models.IntegerField(_("duration"))
    facilities = models.TextField(_("facilities"), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("package")
        verbose_name_plural = _("packages")


class Hotel(BaseModel):
    name = models.CharField(_("name"), max_length=100)
    description = models.TextField(_("description"), blank=True)
    image = models.ImageField(
        _("image"), upload_to="images/hotel/", default="images/hotel/default.jpg"
    )
    location = models.CharField(_("location"), max_length=100)
    city = models.CharField(_("city"), max_length=100)
    price = models.FloatField(_("price per night"), default=1000)
    rating = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("hotel")
        verbose_name_plural = _("hotels")


class ImageModel(BaseModel):
    """Abstract model for image relationships"""

    image = models.ImageField(_("image"), upload_to="images/")

    class Meta:
        abstract = True


class TripImage(ImageModel):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="images")


class HotelImage(ImageModel):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="images")
    upload_to = "images/hotel_images/"
    default = "images/hotel_images/default.jpg"

    def __str__(self):
        return f"{self.hotel.name} Image"


class PackageImage(ImageModel):
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE, related_name="images"
    )
    upload_to = "images/package_images/"
    default = "images/package_images/default.jpg"


class ActivityImage(ImageModel):
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="images"
    )
    upload_to = "images/activity_images/"
    default = "images/activity_images/default.jpg"


class TripBooking(BookingBaseModel):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="bookings")

    def __str__(self):
        return f"{self.trip.destination.name} booking by {self.user.email}"

    @classmethod
    def get_booking_type(cls):
        return "Trip"

    def get_booked_instance(self):
        return self.trip


class ActivityBooking(BookingBaseModel):
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="bookings"
    )

    def __str__(self):
        return f"{self.activity.name} booking by {self.user.email}"

    @classmethod
    def get_booking_type(cls):
        return "Activity"

    def get_booked_instance(self):
        return self.activity


class HotelBooking(BookingBaseModel):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="bookings")
    to_date = models.DateField(_("to date"))

    def __str__(self):
        return f"{self.hotel.name} booking by {self.user.email}"

    @classmethod
    def get_booking_type(cls):
        return "Hotel"

    def get_booked_instance(self):
        return self.hotel


class PackageBooking(BookingBaseModel):
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE, related_name="bookings"
    )

    def __str__(self):
        return f"{self.package.name} booking by {self.user.email}"

    @classmethod
    def get_booking_type(cls):
        return "Package"

    def get_booked_instance(self):
        return self.package


class FavouriteTrip(FavouriteBaseModel):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="favourites")

    class Meta(FavouriteBaseModel.Meta):
        verbose_name = _("favorite trip")
        verbose_name_plural = _("favorite trips")
        unique_together = (("user", "trip"),)


class FavouriteDestination(FavouriteBaseModel):
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name="favourites"
    )

    class Meta(FavouriteBaseModel.Meta):
        verbose_name = _("favorite destination")
        verbose_name_plural = _("favorite destinations")
        unique_together = (("user", "destination"),)


class FavouriteHotel(FavouriteBaseModel):
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name="favourites"
    )

    class Meta(FavouriteBaseModel.Meta):
        verbose_name = _("favorite hotel")
        verbose_name_plural = _("favorite hotels")
        unique_together = (("user", "hotel"),)


class FavouritePackage(FavouriteBaseModel):
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE, related_name="favourites"
    )

    class Meta(FavouriteBaseModel.Meta):
        verbose_name = _("favorite package")
        verbose_name_plural = _("favorite packages")
        unique_together = (("user", "package"),)


class FavouriteActivity(FavouriteBaseModel):
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="favourites"
    )

    class Meta(FavouriteBaseModel.Meta):
        verbose_name = _("favorite activity")
        verbose_name_plural = _("favorite activities")
        unique_together = (("user", "activity"),)


class TripReview(ReviewBaseModel):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"Review for {self.trip} by {self.user.email}"


class ActivityReview(ReviewBaseModel):
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="reviews"
    )

    def __str__(self):
        return f"Review for {self.activity} by {self.user.email}"


class HotelReview(ReviewBaseModel):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"Review for {self.hotel} by {self.user.email}"


class PackageReview(ReviewBaseModel):
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE, related_name="reviews"
    )

    def __str__(self):
        return f"Review for {self.package} by {self.user.email}"
