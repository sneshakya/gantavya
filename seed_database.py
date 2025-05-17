import os
import django
from faker import Faker
from random import randint, choice
from decimal import Decimal
from datetime import timedelta

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gantavya.settings")
django.setup()

from accounts.models import CustomUser
from trips.models import (
    Activity,
    Destination,
    Hotel,
    Package,
    Trip,
    TripReview,
    TripBooking,
    FavouriteTrip,
)

fake = Faker()


def clean_database():
    """Delete all existing records from the database"""
    print("Cleaning database...")
    models = [
        CustomUser,
        Destination,
        Trip,
        TripReview,
        TripBooking,
        FavouriteTrip,
        Hotel,
        Activity,
        Package,
    ]

    for model in models:
        model.objects.all().delete()
    print("Database cleaned!")


def create_destinations(num_destination: int = 10):
    """Create destination records"""
    print(f"Creating {num_destination} destinations...")
    for _ in range(num_destination):
        Destination.objects.create(
            name=fake.city(),
            description=fake.text(max_nb_chars=200),
            longitude=Decimal(str(fake.longitude())),
            latitude=Decimal(str(fake.latitude())),
            city=fake.city(),
            location=fake.address(),
        )
    print("Destinations created!")


def create_trips(num_trips: int = 20):
    """Create trip records"""
    print("Creating trips...")
    destinations = list(Destination.objects.all())
    if not destinations:
        print("No destinations found! Please create destinations first.")
        return

    for _ in range(num_trips):
        destination = choice(destinations)
        Trip.objects.create(
            name=fake.city(),
            destination=destination,
            description=fake.text(max_nb_chars=500),
            price=Decimal(randint(1000, 10000)),
            travelling_days=randint(1, 14),
        )
    print("Trips created!")


def create_users(num_user: int = 10):
    """Create user records"""
    print(f"Creating {num_user} users...")
    for _ in range(num_user):
        phone_number = fake.phone_number()[:10]  # Ensure 10 digit phone number
        CustomUser.objects.create_user(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            username=fake.user_name(),
            email=fake.email(),
            phone_number=phone_number,
            dob=fake.date_of_birth(minimum_age=18, maximum_age=65),
            address=fake.address(),
            password="password123",
        )
    print("Users created!")


def create_trip_reviews():
    """Create trip review records"""
    print("Creating trip reviews...")
    trips = list(Trip.objects.all())
    users = list(CustomUser.objects.all())

    if not trips or not users:
        print("No trips or users found! Please create trips and users first.")
        return

    for trip in trips:
        for _ in range(randint(1, 10)):
            TripReview.objects.create(
                trip=trip,
                comment=fake.text(max_nb_chars=300),
                rating=randint(1, 5)
            )
    print("Trip reviews created!")


def create_hotels(num_hotels: int = 10):
    """Create hotel records"""
    print(f"Creating {num_hotels} hotels...")
    for _ in range(num_hotels):
        Hotel.objects.create(
            name=fake.company(),
            description=fake.text(max_nb_chars=200),
            location=fake.address(),
            city=fake.city(),
            price=randint(1000, 5000),
            rating=randint(1, 5),
        )
    print("Hotels created!")


def create_activities(num_activities: int = 10):
    """Create activity records"""
    print(f"Creating {num_activities} activities...")
    for _ in range(num_activities):
        Activity.objects.create(
            name=fake.word(),
            description=fake.text(max_nb_chars=200),
            location=fake.address(),
            city=fake.city(),
            price=randint(500, 2000),
        )
    print("Activities created!")


def create_packages(num_packages: int = 10):
    """Create package records"""
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


if __name__ == "__main__":
    try:
        clean_database()
        create_users(num_user=10)
        create_destinations(num_destination=10)
        create_trips(num_trips=20)
        create_hotels(num_hotels=10)
        create_activities(num_activities=10)
        create_packages(num_packages=10)
        create_trip_reviews()
        print("Database cleaned and populated with dummy data!")
    except Exception as e:
        print(f"Error occurred while populating database: {str(e)}")
