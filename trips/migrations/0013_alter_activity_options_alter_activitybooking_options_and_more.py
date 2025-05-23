# Generated by Django 5.0 on 2025-03-04 19:29

import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
        ('trips', '0012_activitybooking_start_date_hotelbooking_from_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ('-created_at',), 'verbose_name': 'activity', 'verbose_name_plural': 'activities'},
        ),
        migrations.AlterModelOptions(
            name='activitybooking',
            options={'ordering': ('-start_date',)},
        ),
        migrations.AlterModelOptions(
            name='activityreview',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='destination',
            options={'verbose_name': 'destination', 'verbose_name_plural': 'destinations'},
        ),
        migrations.AlterModelOptions(
            name='favouriteactivity',
            options={'verbose_name': 'favorite activity', 'verbose_name_plural': 'favorite activities'},
        ),
        migrations.AlterModelOptions(
            name='favouritedestination',
            options={'verbose_name': 'favorite destination', 'verbose_name_plural': 'favorite destinations'},
        ),
        migrations.AlterModelOptions(
            name='favouritehotel',
            options={'verbose_name': 'favorite hotel', 'verbose_name_plural': 'favorite hotels'},
        ),
        migrations.AlterModelOptions(
            name='favouritepackage',
            options={'verbose_name': 'favorite package', 'verbose_name_plural': 'favorite packages'},
        ),
        migrations.AlterModelOptions(
            name='favouritetrip',
            options={'verbose_name': 'favorite trip', 'verbose_name_plural': 'favorite trips'},
        ),
        migrations.AlterModelOptions(
            name='hotel',
            options={'verbose_name': 'hotel', 'verbose_name_plural': 'hotels'},
        ),
        migrations.AlterModelOptions(
            name='hotelbooking',
            options={'ordering': ('-start_date',)},
        ),
        migrations.AlterModelOptions(
            name='hotelreview',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='package',
            options={'verbose_name': 'package', 'verbose_name_plural': 'packages'},
        ),
        migrations.AlterModelOptions(
            name='packagebooking',
            options={'ordering': ('-start_date',)},
        ),
        migrations.AlterModelOptions(
            name='packagereview',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='trip',
            options={'verbose_name': 'trip', 'verbose_name_plural': 'trips'},
        ),
        migrations.AlterModelOptions(
            name='tripbooking',
            options={'ordering': ('-start_date',)},
        ),
        migrations.AlterModelOptions(
            name='tripreview',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RemoveField(
            model_name='activityreview',
            name='user',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='travelling_days',
        ),
        migrations.RemoveField(
            model_name='hotelbooking',
            name='from_date',
        ),
        migrations.RemoveField(
            model_name='hotelreview',
            name='user',
        ),
        migrations.RemoveField(
            model_name='packagereview',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tripreview',
            name='user',
        ),
        migrations.AddField(
            model_name='activity',
            name='price',
            field=models.FloatField(default=1000),
        ),
        migrations.AddField(
            model_name='activity',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='activitybooking',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='activitybooking',
            name='transaction_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.paymenthistory'),
        ),
        migrations.AddField(
            model_name='activitybooking',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='activityimage',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='activityreview',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='favouriteactivity',
            name='created_at',
            field=models.DateField(auto_now_add=True, default='1111-11-11', verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favouriteactivity',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='favouriteactivity',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='favouritedestination',
            name='created_at',
            field=models.DateField(auto_now_add=True, default='1111-11-11', verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favouritedestination',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='favouritedestination',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='favouritehotel',
            name='created_at',
            field=models.DateField(auto_now_add=True, default='1111-11-11', verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favouritehotel',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='favouritehotel',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='favouritepackage',
            name='created_at',
            field=models.DateField(auto_now_add=True, default='1111-11-11', verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favouritepackage',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='favouritepackage',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='favouritetrip',
            name='created_at',
            field=models.DateField(auto_now_add=True, default='1111-11-11', verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favouritetrip',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='favouritetrip',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='price',
            field=models.FloatField(default=1000, verbose_name='price per night'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='start_date',
            field=models.DateField(default='1111-11-11', verbose_name='start date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='transaction_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.paymenthistory'),
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='hotelimage',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='hotelreview',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='package',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='packagebooking',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='packagebooking',
            name='transaction_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.paymenthistory'),
        ),
        migrations.AddField(
            model_name='packagebooking',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='packageimage',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='packagereview',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='trip',
            name='description',
            field=models.CharField(default='Description', max_length=500, verbose_name='trip description'),
        ),
        migrations.AddField(
            model_name='trip',
            name='name',
            field=models.CharField(default='trip', max_length=50, verbose_name='trip name'),
        ),
        migrations.AddField(
            model_name='trip',
            name='travelling_days',
            field=models.IntegerField(default=0, verbose_name='travelling days'),
        ),
        migrations.AddField(
            model_name='tripbooking',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='tripbooking',
            name='transaction_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.paymenthistory'),
        ),
        migrations.AddField(
            model_name='tripbooking',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='tripimage',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AddField(
            model_name='tripimage',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='tripreview',
            name='product_code',
            field=models.CharField(default=uuid.UUID('e93639ba-f92e-11ef-8018-e470b8d26680'), editable=False, max_length=100, verbose_name='product code'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='city',
            field=models.CharField(max_length=100, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=models.ImageField(default='images/activities/default.jpg', upload_to='images/activities/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='location',
            field=models.CharField(max_length=100, verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='activitybooking',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='trips.activity'),
        ),
        migrations.AlterField(
            model_name='activitybooking',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='activitybooking',
            name='start_date',
            field=models.DateField(verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='activitybooking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activityimage',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='trips.activity'),
        ),
        migrations.AlterField(
            model_name='activityimage',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='activityimage',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='activityimage',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='activityreview',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='trips.activity'),
        ),
        migrations.AlterField(
            model_name='activityreview',
            name='comment',
            field=models.TextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='activityreview',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='activityreview',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='rating'),
        ),
        migrations.AlterField(
            model_name='activityreview',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='city',
            field=models.CharField(max_length=100, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.ImageField(default='images/destination/default.jpg', upload_to='images/destination/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=10, verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='location',
            field=models.CharField(max_length=100, verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=10, verbose_name='longitude'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='favouriteactivity',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to='trips.activity'),
        ),
        migrations.AlterField(
            model_name='favouriteactivity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favouritedestination',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to='trips.destination'),
        ),
        migrations.AlterField(
            model_name='favouritedestination',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favouritehotel',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to='trips.hotel'),
        ),
        migrations.AlterField(
            model_name='favouritehotel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favouritepackage',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to='trips.package'),
        ),
        migrations.AlterField(
            model_name='favouritepackage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favouritetrip',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to='trips.trip'),
        ),
        migrations.AlterField(
            model_name='favouritetrip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=models.CharField(max_length=100, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.ImageField(default='images/hotel/default.jpg', upload_to='images/hotel/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='location',
            field=models.CharField(max_length=100, verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='trips.hotel'),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='to_date',
            field=models.DateField(verbose_name='to date'),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hotelimage',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='hotelimage',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='trips.hotel'),
        ),
        migrations.AlterField(
            model_name='hotelimage',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='hotelimage',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='hotelreview',
            name='comment',
            field=models.TextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='hotelreview',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='hotelreview',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='trips.hotel'),
        ),
        migrations.AlterField(
            model_name='hotelreview',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='rating'),
        ),
        migrations.AlterField(
            model_name='hotelreview',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='package',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='package',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='package',
            name='duration',
            field=models.IntegerField(verbose_name='duration'),
        ),
        migrations.AlterField(
            model_name='package',
            name='facilities',
            field=models.TextField(blank=True, verbose_name='facilities'),
        ),
        migrations.AlterField(
            model_name='package',
            name='image',
            field=models.ImageField(default='images/package/default.jpg', upload_to='images/package/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='package',
            name='location',
            field=models.CharField(max_length=100, verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='package',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='package',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='packagebooking',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='packagebooking',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='trips.package'),
        ),
        migrations.AlterField(
            model_name='packagebooking',
            name='start_date',
            field=models.DateField(verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='packagebooking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='packageimage',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='packageimage',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='packageimage',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='trips.package'),
        ),
        migrations.AlterField(
            model_name='packageimage',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='packagereview',
            name='comment',
            field=models.TextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='packagereview',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='packagereview',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='trips.package'),
        ),
        migrations.AlterField(
            model_name='packagereview',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='rating'),
        ),
        migrations.AlterField(
            model_name='packagereview',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='trips.destination'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='image',
            field=models.ImageField(default='images/trip/default.jpg', upload_to='images/trip/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='tripbooking',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='tripbooking',
            name='start_date',
            field=models.DateField(verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='tripbooking',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='trips.trip'),
        ),
        migrations.AlterField(
            model_name='tripbooking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tripimage',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='tripimage',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='tripimage',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='trips.trip'),
        ),
        migrations.AlterField(
            model_name='tripreview',
            name='comment',
            field=models.TextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='tripreview',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='tripreview',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='rating'),
        ),
        migrations.AlterField(
            model_name='tripreview',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='trips.trip'),
        ),
        migrations.AlterField(
            model_name='tripreview',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterUniqueTogether(
            name='favouriteactivity',
            unique_together={('user', 'activity')},
        ),
        migrations.AlterUniqueTogether(
            name='favouritedestination',
            unique_together={('user', 'destination')},
        ),
        migrations.AlterUniqueTogether(
            name='favouritehotel',
            unique_together={('user', 'hotel')},
        ),
        migrations.AlterUniqueTogether(
            name='favouritepackage',
            unique_together={('user', 'package')},
        ),
        migrations.AlterUniqueTogether(
            name='favouritetrip',
            unique_together={('user', 'trip')},
        ),
    ]
