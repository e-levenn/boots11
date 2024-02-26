from django.urls import path
from Myapp import views
urlpatterns = [
    path('', views.home, name='my_index'),
    path('blog/', views.blog, name='my_blog'),
    path('contact/', views.contact, name='my_contact'),
    path('main/', views.main, name='my_main'),
    path('blog/', views.blog, name='my_blog'),
    path('matches/', views.matches, name='my_matches'),
    path('players/', views.players, name='my_players'),
    path('single/', views.single, name='my_single'),


]