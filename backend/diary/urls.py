from django.urls import path
from . import views

urlpatterns = [
    path('user', views.user, name='user'),
    path('user/<int:id>',views.user_detail, name='user_detail'),
]
