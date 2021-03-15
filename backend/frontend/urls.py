from django.urls import path 
from . import views
urlpatterns=[
    path('signup', views.signup, name="signup"),
    path('Show_data', views.Show_data, name="Show_data"),
    path('login', views.login, name="login"),
    path('addf', views.addf, name="addf"),
    path('Show_fur', views.Show_fur, name="Show_fur")
]