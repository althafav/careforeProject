

from . import views
from django.urls import path


urlpatterns = [

    path('place_order', views.place_order, name='place_order'),
    path('payment_page', views.payment_page, name='payment_page'),
    
    
    path('proceed-to-pay', views.razorpaycheck),
    path('payments', views.payments, name="payments"),
   
    
 
] 
