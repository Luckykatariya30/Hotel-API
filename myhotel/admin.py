from django.contrib import admin
from .models import Hotel , HotelImage, Amenities
# Register your models here.

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name','hotel_price']

@admin.register(HotelImage)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel','image']

@admin.register(Amenities)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['amenities']
    