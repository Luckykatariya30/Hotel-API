from django.db import models


class Amenities(models.Model):
    amenities = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.amenities




class Hotel(models.Model):
    hotel_name = models.CharField(max_length=121)
    hotel_price = models.IntegerField()
    hotel_description = models.TextField()
    amenities = models.ManyToManyField(Amenities)

    banner_image = models.ImageField(upload_to='hotels')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.hotel_name
    
    def get_amenities(self):
        payload = []
        for i in self.amenities.all():
            payload.append({
                'id':i.id,
                'amenity':i.amenities
            })
        return payload




class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotels')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.hotel.hotel_name
