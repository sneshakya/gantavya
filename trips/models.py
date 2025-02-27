from django.db import models

from accounts.models import CustomUser


# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/destination/", default="images/destination/default.jpg"
    )
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    travelling_days = models.IntegerField()

    def __str__(self):
        return self.name


class Trip(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="images/trip/", default="images/trip/default.jpg"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.destination.name


class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/activities/", default="images/activities/default.jpg"
    )
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/package/", default="images/package/default.jpg"
    )
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    duration = models.IntegerField()
    facilities = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/hotel/", default="images/hotel/default.jpg"
    )
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


# Images
class TripImage(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    created_at = models.DateField(auto_now_add=True)


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="images/hotel_images/", default="images/hotel_images/default.jpg"
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class PackageImage(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="images/package_images/", default="images/package_images/default.jpg"
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class ActivityImage(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="images/activity_images/",
        default="images/activity_images/default.jpg",
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


# Bookings
class TripBooking(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "trip"


class ActivityBooking(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return "activity"


class HotelBooking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "hotel"


class PackageBooking(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "package"


# Favourites
class FavouriteTrip(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class FavouriteDestination(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class FavouriteHotel(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class FavouritePackage(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class FavouriteActivity(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


# Reviews
class TripReview(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class ActivityReview(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class HotelReview(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class PackageReview(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
