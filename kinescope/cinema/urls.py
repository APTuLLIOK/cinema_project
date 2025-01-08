from django.urls import path
from . import views


app_name = 'cinema'

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('sessions/<int:session_id>/',
         views.session_detail,
         name='session_detail'),
    path('sessions/', views.session_list, name='session_list'),
]
