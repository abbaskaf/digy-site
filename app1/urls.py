from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('about', views.AboutView, name='about'),
    path('<int:pk>', views.DetaView.as_view(), name='detail'),
    path('Logout', views.LogoutUser, name='Logout'),
    path('Login', views.LoginUser, name='Login'),
    path('signup', views.SignUp, name='sign'),
    path('category/<str:cate>', views.CategoryView, name='category')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
