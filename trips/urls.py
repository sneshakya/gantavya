from django.urls import path, include

from . import views

urlpatterns = [
	path( 'explore/', views.index, name = "explore" ),
]
