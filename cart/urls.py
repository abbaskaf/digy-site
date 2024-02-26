from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartView,name='Cart'),
    path('', views.AddView,name='AddCart'),
    path('', views.DeleteView,name='DeleteCart'),
    path('', views.EditView,name='EditCart'),
]
