from django.urls import path, include

from . import views


urlpatterns = [
	path( 'explore/', views.index, name="explore" ),
	path( 'add-to-favourites/', views.add_to_favourites, name="add_to_favourites" ),
 
	path( 'destination/', views.destinations, name="destination" ),
	path( 'destination/<int:id>/', views.destinations, name="destination" ),

	path( 'hotels/', views.hotels, name="hotels" ),
	path( 'hotels/<int:id>/', views.hotels, name="hotels" ),

	path( 'activities/', views.activities, name="activities" ),
	path( 'activities/<int:id>/', views.activities, name="activities" ),

	path( 'packages/', views.packages, name="packages" ),
	path( 'packages/<int:id>/', views.packages, name="packages" ),
]
