from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.services, name='services'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('services/', views.services, name='services'),
#     path('booking/', views.booking, name='booking'),
#     path('contact/', views.contact, name='contact'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     path('register/', views.register, name='register'),
# ]