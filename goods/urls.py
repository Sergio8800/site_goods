from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', GoodsList.as_view(), name='goods_list_url'),
    path('add-new-car/', AddCar_View.as_view(), name='add_car_new'),
    path('update-new-car/rec/<int:pk>/', Update_Car_View.as_view(), name='update_car_new'),
    path('delete-new-car/rec/<int:pk>/', delete_car, name='delete_car_new'),
    path('login/', MyLoginUserView.as_view(), name='login_my'),
    path('register/', MyRegisterUserView.as_view(), name='register_my'),
    path('logout/', MyLogoutView.as_view(), name='logout_my'),

    path("add-rating/", AddStars.as_view(), name='add_rating'),
    path('<str:slug>/', CarDetail.as_view(), name='car_detail_url'),
    path('rec/<int:pk>/', AddReview.as_view(), name='add_review'),

]
