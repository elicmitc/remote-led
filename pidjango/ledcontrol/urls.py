from django.urls import path
from . import views

urlpatterns = [
    # ex: /ledcontrol/
    path('',views.index,name='index'),
    path('rgb/<str:r>/<str:g>/<str:b>/',views.rgb,name='rgb') 
        ]
