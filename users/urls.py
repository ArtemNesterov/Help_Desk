from django.urls import path

from django.contrib.auth.views import LoginView

from users import views

urlpatterns = [

    path('register/', views.Register.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
]
