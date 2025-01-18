from django.urls import path, include

from . import views


urlpatterns = [
	path( 'explore/', views.index, name="explore" ),
	path( 'destination/', views.destinations, name="destination" ),
	path( 'destination/<int:id>/', views.destinations, name="destination" ),
]
