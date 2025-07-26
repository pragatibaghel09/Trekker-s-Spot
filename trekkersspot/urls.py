from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.home ,name='home' ),
    path('home',views.home ,name='home' ),
    path('registration',views.registration ,name='registration'),
    path('aboutus',views.aboutus ,name='aboutus' ),
    path('HPT',views.HPT ,name='HPT' ),
    path('contactus',views.contactus ,name='contactus' ),
    path('payment',views.payment ,name='payment' ),
    path('sucess',views.sucess,name='sucess'),
    path('alltreks',views.alltreks, name='alltreks' ),
    path('feedback',views.feedback, name ='feedback')
  
]
               
               
               
    
    

