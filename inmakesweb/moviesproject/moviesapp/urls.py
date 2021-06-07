
from django.urls import path

from .import views
app_name='movieapp'
urlpatterns = [

    path('',views.example,name='example'),
    path('movie/<int:movieid>/',views.detailss,name='detailss'),
    path('add/',views.add_movie,name='add_movie'),
    path('edit/<int:id>/',views.updatee,name='updatee'),
    path('delete/<int:id>/',views.deletee,name='deletee')
]
