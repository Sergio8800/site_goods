from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('', GoodsList.as_view(), name='goods_list_url'),
    path('add-new-car/', addcar, name='add_car'),



    path('add-new/', AddCar.as_view(), name='add_car_new'),



    path("add-rating/", AddStars.as_view(), name='add_rating'),
    path('<str:slug>/', CarDetail.as_view(), name='car_detail_url'),
    path('rec/<int:pk>/', AddReview.as_view(), name='add_review'),


]
