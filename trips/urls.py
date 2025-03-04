from django.urls import path

from . import views

urlpatterns = [
    path("explore/", views.index, name="explore"),
    path("add-to-favourites/", views.add_to_favourites, name="add_to_favourites"),
    
    path("destinations/", views.destinations, name="destinations_list"),
    path("destinations/<int:id>/", views.destinations, name="destination_detail"),
    path("hotels/", views.hotels, name="hotels_list"),
    path("hotels/<int:id>/", views.hotels, name="hotel_detail"),
    path("activities/", views.activities, name="activities_list"),
    path("activities/<int:id>/", views.activities, name="activity_detail"),
    path("packages/", views.packages, name="packages_list"),
    path("packages/<int:id>/", views.packages, name="package_detail"),
    
    path("add-booking/", views.add_booking, name="add_booking"),
    path("bookings/", views.total_booking, name="total_booking"),
    path("booking-detail/<int:id>/", views.booking_detail, name="booking_detail"),
    path("book-trip/", views.book_trip, name="book_trip"),
    path("book-activity/", views.book_activity, name="book_activity"),
    path("book-package/", views.book_package, name="book_package"),
    path("book-hotel/", views.book_hotel, name="book_hotel")
    
]
