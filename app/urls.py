from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_timers, name='timers'),
    path('add_timer/<int:id>', views.add, name='add_timer'),
]