from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('edit_user', views.edit_user, name='edit_user'),
    path('dash', views.dash_bord, name='dashbord'),
]
