from django.urls import path
from . import views


app_name = 'cinema'

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path(
        'profile/<str:username>/',
        views.ProfileView.as_view(),
        name='profile'
    ),
    path(
        'sessions/<int:session_id>/',
        views.session_detail,
        name='session_detail'
    ),
    path('sessions/', views.session_list, name='session_list'),
    path('tickets/<int:session_id>/', views.tickets, name='tickets'),
    path('tickets/<int:session_id>/buy/', views.buy_ticket, name='buy_ticket'),
]
