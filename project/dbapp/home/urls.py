

from django.urls import path

from django.contrib import admin 
from django.urls import path, re_path
from dbapp.home import views

urlpatterns = [
    # The home page
    path('', views.index, name='home'),
    path('send/', views.upload , name = 'send'),
    path('card/', views.card, name = 'card'),
    path('card/update/<card_id>', views.update, name='update'),
    path('card/delete/<card_id>', views.delete, name='delete'),
    path('hotels/', views.hotels, name='hotels'),
    path('hotels/add/<hotel_id>', views.hotel_order, name='hotel_order'),
    path('tours/add/<tour_id>', views.tour_order, name='tour_order'),
    path('tours/', views.tours, name='tours'),
    path('hotel_order/', views.gethotel_order, name='gethotel_order'),
    path('hotel_order/delete/<order_id>', views.deletehotel_order, name='deletehotel_order'),
    path('tour_order/', views.gettour_order, name='gettour_order'),
    path('tour_order/delete/<order_id>', views.deletetour_order, name='deletetour_order'),
    # path("search/", views.search, name="search"),
    path("hotelresults/", views.gethotel_search, name="gethotel_search"),
    path("tourresults/", views.gettour_search, name="gettour_search"),
    path("about_us/", views.about_us, name="about_us"),
    # # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]

   





