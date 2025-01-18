from django.db import models

from accounts.models import CustomUser


# Create your models here.
class Destination( models.Model ):
	name = models.CharField( max_length=100 )
	description = models.TextField( blank=True )
	image = models.ImageField( upload_to='images/', blank=True )
	longitude = models.DecimalField( max_digits=10, decimal_places=6 )
	latitude = models.DecimalField( max_digits=10, decimal_places=6 )
	city = models.CharField( max_length=100 )
	location = models.CharField( max_length=100 )


	def __str__( self ):
		return self.name


class Trip( models.Model ):
	title = models.CharField( max_length=100 )
	destination = models.ForeignKey( Destination, on_delete=models.CASCADE )
	description = models.TextField( blank=True )
	image = models.ImageField( upload_to='images/', blank=True )
	price = models.DecimalField( max_digits=10, decimal_places=2 )


	def __str__( self ):
		return self.title


class TripImage( models.Model ):
	trip = models.ForeignKey( Trip, on_delete=models.CASCADE )
	image = models.ImageField( upload_to='images/' )
	created_at = models.DateTimeField( auto_now_add=True )


class TripReview( models.Model ):
	trip = models.ForeignKey( Trip, on_delete=models.CASCADE )
	user = models.ForeignKey( CustomUser, on_delete=models.CASCADE )
	comment = models.TextField()
	rating = models.IntegerField()
	created_at = models.DateTimeField( auto_now_add=True )
	updated_at = models.DateTimeField( auto_now=True )


class TripBooking( models.Model ):
	trip = models.ForeignKey( Trip, on_delete=models.CASCADE )
	user = models.ForeignKey( CustomUser, on_delete=models.CASCADE )
	start_date = models.DateField()
	end_date = models.DateField()
	created_at = models.DateTimeField( auto_now_add=True )


class FavouriteTrip( models.Model ):
	trip = models.ForeignKey( Trip, on_delete=models.CASCADE )
	user = models.ForeignKey( CustomUser, on_delete=models.CASCADE )
