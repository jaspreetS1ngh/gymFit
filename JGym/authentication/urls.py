from django.urls import path
from authentication import views

urlpatterns = [
    
    path('',views.Home,name= "Home" ),
    path('SignUp', views.SignUp, name="SignUp"),
    path('HandleLogin', views.handleLogin, name="handleLogin"),
    path('logout', views.handlelogout, name="handlelogout"),
]
