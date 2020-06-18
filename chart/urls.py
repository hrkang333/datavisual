from django.contrib import admin
from django.urls import path
from chart import views                                     # !!!

urlpatterns = [

    path('ticket-class/3/', views.ticket_class_view_3, name='ticket_class_view_3'),
    path('con_19/', views.con_19, name='con_19'),
    path('dth_19/', views.dth_19, name='dth_19'),
    path('rec_19/', views.rec_19, name='rec_19'),
    path('admin/', admin.site.urls),
]
