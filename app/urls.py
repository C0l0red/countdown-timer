from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_timers, name='show_timers'),
    path('add_timer/<int:id>', views.add, name='add_timer'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]