from django.urls import path
from .views import Add_hotel, List_hotel, Detail_hotel, Update_hotel, Delete_hotel

urlpatterns = [
    path('add/', Add_hotel.as_view()),
    path('list/', List_hotel.as_view()),
    path('detail/<int:pk>/', Detail_hotel.as_view()),
    path('update/<int:pk>/', Update_hotel.as_view()),
    path('delete/<int:pk>/', Delete_hotel.as_view()),
]
