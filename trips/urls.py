from django.urls import path, include

from . import views


urlpatterns = [
    path("explore/", views.index, name="explore"),
    path("add-to-favourites/", views.add_to_favourites, name="add_to_favourites"),
    path("destinations/", views.destinations, name="destinations"),
    path("destinations/<int:id>/", views.destinations, name="destinations"),
    path("hotels/", views.hotels, name="hotels"),
    path("hotels/<int:id>/", views.hotels, name="hotels"),
    path("activities/", views.activities, name="activities"),
    path("activities/<int:id>/", views.activities, name="activities"),
    path("packages/", views.packages, name="packages"),
    path("packages/<int:id>/", views.packages, name="packages"),
    path("book-trip/<int:id>", views.book_trip, name="book_trip"),
    path("book-activity/<int:id>", views.book_activity, name="book_activity"),
    path("book-package/<int:id>", views.book_package, name="book_package"),
    path("bookings/", views.bookings, name="bookings"),
]
