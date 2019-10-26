from django.urls import path
from . import views
from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns =[

    path("regester",views.regester, name="regester"),
    path("logout",views.logout,name="logout"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("login" ,views.login, name="login"),
    path("destinations", views.destinations,name="destinations"),
]