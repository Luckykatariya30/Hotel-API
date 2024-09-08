from django.shortcuts import render
from .models import Hotel ,HotelImage , Amenities
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request , 'myhotel/hotel.html')
def hotel(request):
    try:
        hotel_obj = Hotel.objects.all()
        
        if request.GET.get('sort_by'):
            sort_by_value = request.GET.get('sort_by')
            if sort_by_value == 'asc' :
                hotel_obj = hotel_obj.order_by('hotel_price')
            elif sort_by_value == 'dsc':
                hotel_obj = hotel_obj.order_by('-hotel_price')
        if request.GET.get('amount'):
            amount = request.GET.get('amount')
            hotel_obj = hotel_obj.filter(hotel_price__lte = amount)

        if request.GET.get('amenities'):
            amenities = request.GET.get('amenities')
            amenities = str(amenities).split(',')
            an = []
            for i in amenities:
                an.append(int(i))
            hotel_obj = hotel_obj.filter(amenities__in = an).distinct()

        payload = []
        for i in hotel_obj:
            payload.append({
                'hotel_name':i.hotel_name,
                'hotel_price':i.hotel_price,
                'hotel_des':i.hotel_description,
                'hotel_image':str(i.banner_image),
                'amenities':i.get_amenities(),
                })
            

    
        return JsonResponse(payload , safe=False)
    
    except Exception as e:
        print(e)

    return JsonResponse({'message':'some is wrong......'})