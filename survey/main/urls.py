from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from main import views
urlpatterns = [
    path('',views.inde,name=''),
    path('hom/',views.index,name="hom"),
    path('administrator/',views.disp,name="administrator"),
    path('administrator/process_login/',views.process_login,name="administrator/process_login"),
    path('get_data/',views.gets,name='get_data'),
    path('third.html/',views.third,name='third.html'),
    path('third.html/thirs/',views.thirs,name='thirs'),
    path('third.html/thirs/fourth/',views.fourth,name='third.html/thirs/fourth/'),
    path('third.html/thirs/fourth/fifth/',views.fifth,name='third.html/thirs/fourth/fifth'),
    path('third.html/thirs/fourth/fifth/sixth',views.sixth,name='third.html/thirs/fourth/fifth/sixth'),
    path('third.html/thirs/fourth/fifth/index.html',views.inde,name='third.html/thirs/fourth/fifth/sixth/index.html'),
    
]