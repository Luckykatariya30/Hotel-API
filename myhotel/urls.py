from django.urls import path
from myhotel import views

urlpatterns = [
    path('',views.hotel , name="hotel"),
    path('home/',views.home , name="home")
]