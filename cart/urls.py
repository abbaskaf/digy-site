from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartView, name='CartCart'),
    path('add/', views.AddView, name='AddCart'),
    path('delete/', views.DeleteView, name='DeleteCart'),
    path('edite/', views.EditView, name='EditCart'),
]
