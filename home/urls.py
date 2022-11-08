from django.contrib import admin
from django.urls import path
from home.views import Home
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Home, name='home'),
    path('saveinfo/', views.Saveinfo, name='Saveinfo'),
    path('login/', views.Login, name='login'), 
    path('logout/', views.Logout, name='logout'), 
    path('main/', views.main, name='main'),
    path('admin/', views.admin, name='admin'),
    path('index/', views.index, name='index'),
    path('teacher/', views.teacher, name='teacher'),
    path('saveinfo_teacher/', views.Saveinfo_teacher, name='Saveinfo_teacher'),
    path('showvideo/', views.showvideo, name='showvideo'),
    path('aasd/', views.aasd, name='aasd'),
    path('pay/', views.Pay, name='pay'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)