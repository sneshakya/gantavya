import os
import django
from faker import Faker
from random import randint, choice
from decimal import Decimal
from datetime import timedelta


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gantavya.settings")
django.setup()

from accounts.models import CustomUser
from trips.models import (
    Activities,
    Destination,
    Hotel,
    Package,
    Trip,
    TripImage,
    TripReview,
    TripBooking,
    FavouriteTrip,
)


fake = Faker()


# Populate destinations
def create_destinations(num_destination: int = 10):
    print(f"Creating {num_destination} destinations...")
    for _ in range(num_destination):
        Destination.objects.create(
            name=fake.city(),
            description=fake.text(max_nb_chars=200),
            longitude=fake.longitude(),
            latitude=fake.latitude(),
            city=fake.city(),
            location=fake.address(),
        )
    print("Destinations created!")


# Populate trips
def create_trips(num_trips: int = 20):
    print("Creating trips...")
    destinations = Destination.objects.all()
    for _ in range(num_trips):
        destination = choice(destinations)
        Trip.objects.create(
            title=fake.sentence(),
            destination=destination,
            description=fake.text(max_nb_chars=300),
            price=Decimal(randint(1000, 10000)),  # Price between 1000 and 10000
        )
    print("Trips created!")


# Populate trip images
def create_trip_images():
    print("Creating trip images...")
    trips = Trip.objects.all()
    for trip in trips:
        for _ in range(randint(1, 5)):  # 1 to 5 images per trip
            TripImage.objects.create(
                trip=trip,
            )
    print("Trip images created!")


# Populate users
def create_users(num_user: int = 10):
    print(f"Creating {num_user} users...")
    for _ in range(num_user):
        phone_number = fake.phone_number()
        phone_number = phone_number[:10]

        CustomUser.objects.create_user(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            username=fake.user_name(),
            email=fake.email(),
            phone_number=phone_number,
            dob=fake.date_of_birth(
                minimum_age=18, maximum_age=65
            ),  # Age between 18 and 65
            address=fake.address(),
            password="password123",  # Default password
        )
    print("Users created!")


# Populate trip reviews
def create_trip_reviews():
    print("Creating trip reviews...")
    trips = Trip.objects.all()
    users = CustomUser.objects.all()
    for trip in trips:
        for _ in range(randint(1, 10)):  # 1 to 10 reviews per trip
            TripReview.objects.create(
                trip=trip,
                user=choice(users),
                rating=randint(1, 5),  # Rating from 1 to 5
                comment=fake.text(max_nb_chars=300),
            )
    print("Trip reviews created!")


# Populate trip bookings
def create_trip_bookings():
    print("Creating trip bookings...")
    trips = Trip.objects.all()
    users = CustomUser.objects.all()
    for user in users:
        for _ in range(randint(1, 3)):  # 1 to 3 bookings per user
            trip = choice(trips)
            start_date = fake.date_this_year()
            end_date = start_date + timedelta(
                days=randint(3, 14)
            )  # Duration: 3 to 14 days
            TripBooking.objects.create(
                trip=trip, user=user, start_date=start_date, end_date=end_date
            )
    print("Trip bookings created!")


# Populate favourite trips
def create_favourite_trips():
    print("Creating favourite trips...")
    trips = Trip.objects.all()
    users = CustomUser.objects.all()
    for user in users:
        for _ in range(randint(1, 5)):  # 1 to 5 favourite trips per user
            FavouriteTrip.objects.create(trip=choice(trips), user=user)
    print("Favourite trips created!")


# Populate hotels
def create_hotels(num_hotels: int = 10):
    print(f"Creating {num_hotels} hotels...")
    for _ in range(num_hotels):
        Hotel.objects.create(
            name=fake.company(),
            description=fake.text(max_nb_chars=200),
            location=fake.address(),
            city=fake.city(),
        )
    print("Hotels created!")


# Populate activities
def create_activities(num_activities: int = 10):
    print(f"Creating {num_activities} activities...")
    for _ in range(num_activities):
        Activities.objects.create(
            name=fake.word(),
            description=fake.text(max_nb_chars=200),
            location=fake.address(),
            city=fake.city(),
        )
    print("Activities created!")


# Populate packages
def create_packages(num_packages: int = 10):
    print(f"Creating {num_packages} packages...")
    for _ in range(num_packages):
        Package.objects.create(
            name=fake.word(),
            description=fake.text(max_nb_chars=200),
            location=fake.address(),
            price=Decimal(randint(1000, 10000)),
            duration=randint(1, 7),
            facilities=fake.text(max_nb_chars=200),
        )
    print("Packages created!")


# Main script execution
if __name__ == "__main__":
    create_users(num_user=10)  # Create 10 users
    create_destinations(num_destination=10)  # Create 10 destinations
    create_trips(num_trips=20)  # Create trips based on destinations
    create_trip_images()  # Create images for trips
    create_trip_reviews()  # Create reviews for trips
    create_trip_bookings()  # Create bookings for users
    create_favourite_trips()  # Create favourite trips for users
    create_hotels(num_hotels=10)  # Create 10 hotels
    create_activities(num_activities=10)  # Create 10 activities
    create_packages(num_packages=10)  # Create 10 packages
    print("Database populated with dummy data!")
