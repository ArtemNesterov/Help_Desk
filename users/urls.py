from sys import path

from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view, name='login'),
    path('logout/', views.logout, name='logout'),
]
