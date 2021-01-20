from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='library_app.home'),
    # path('about/', views.about, name='adoption-about'),
   
]