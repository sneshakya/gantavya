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
