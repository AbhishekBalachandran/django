from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login_api'),
    path('borrowedbooks', views.borrowedbooks, name='borrowedbooks_api'),

]