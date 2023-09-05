
from django.urls import path
from .views import *


app_name = "payment"

urlpatterns = [

    path('', IndexView.as_view(), name='home'),
    path('payment/', PaymentView, name='payment'),
    path('payment/success/', CheckoutSuccessView.as_view(), name='success'),
    path('payment/faild/', CheckoutFaildView.as_view(), name='faild'),

]