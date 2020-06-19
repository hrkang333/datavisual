from django.contrib import admin
from django.urls import path
from chart import views                                     # !!!

urlpatterns = [
    path('', views.home, name='home'),  #메인
    path('ticket-class/3/', views.ticket_class_view_3, name='ticket_class_view_3'), #타이타닉
    path('con_19/', views.con_19, name='con_19'),   #코로나 확진자
    path('dth_19/', views.dth_19, name='dth_19'),   #코로나 사망자
    path('rec_19/', views.rec_19, name='rec_19'),   #코로나 회복자
    path('admin/', admin.site.urls),    #관리자
]
