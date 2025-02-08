from django.contrib import admin

from . import models


# Register your models here.
@admin.register( models.Trip )
class TripAdmin( admin.ModelAdmin ):
	empty_value_display = "-empty-"


@admin.register( models.TripImage )
class TripImageAdmin( admin.ModelAdmin ):
	empty_value_display = "-empty-"


@admin.register( models.TripReview )
class TripReviewAdmin( admin.ModelAdmin ):
	empty_value_display = "-empty-"


@admin.register( models.Destination )
class DestinationAdmin( admin.ModelAdmin ):
	empty_value_display = "-empty-"


@admin.register( models.TripBooking )
class TripBookingAdmin( admin.ModelAdmin ):
	empty_value_display = "-empty-"


@admin.register(models.Package)
class PackageAdmin(admin.ModelAdmin):
	empty_value_display = "-empty-"


@admin.register(models.PackageImage)
class PackageImageAdmin(admin.ModelAdmin):
	empty_value_display = "-empty-"


@admin.register(models.PackageReview)
class PackageReviewAdmin(admin.ModelAdmin):
	empty_value_display = "-empty-"


@admin.register(models.Hotel)
class HotelAdmin(admin.ModelAdmin):
	empty_value_display = "-empty-"


@admin.register(models.HotelImage)
class HotelImageAdmin(admin.ModelAdmin):
	empty_value_display = "-empty-"


@admin.register(models.HotelReview)
class HotelReviewAdmin(admin.ModelAdmin):
	empty_value_display = "-empty-"


@admin.register(models.Activities)
class ActivitiesAdmin(admin.ModelAdmin):
	empty_value_display = "-empty-"


@admin.register(models.ActivityImage)
class ActivityImageAdmin(admin.ModelAdmin):
	empty_value_display = "-empty-"


@admin.register(models.ActivityReview)
class ActivityReviewAdmin(admin.ModelAdmin):
	empty_value_display = "-empty-"


@admin.register(models.FavouriteTrip)
class FavouriteTripAdmin(admin.ModelAdmin):
	empty_value_display = "-empty-"


@admin.register(models.FavouriteDestination)
class FavouriteDestinationAdmin(admin.ModelAdmin):
	empty_value_display = "-empty-"


@admin.register(models.FavouriteHotel)
class FavouriteHotelAdmin(admin.ModelAdmin):
	empty_value_display = "-empty-"


@admin.register(models.FavouritePackage)
class FavouritePackageAdmin(admin.ModelAdmin):
	empty_value_display = "-empty-"


@admin.register(models.FavouriteActivity)
class FavouriteActivityAdmin(admin.ModelAdmin):
	empty_value_display = "-empty-"
