from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth import login, authenticate

from django.http import HttpResponse

from django.views.generic import CreateView

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from users.API.serializers import UserSerializer
from users.form import RegisterForm

# Create your views here.
from users.models import User


class UserLogin(LoginView):
    """ login """
    template_name = 'login.html'


class Register(CreateView):
    """ Sign UP """
    form_class = RegisterForm
    success_url = "/login/"
    template_name = "register_page.html"


class UserLogout(LoginRequiredMixin, LogoutView):
    """ Logout """
    next_page = '/'
    redirect_field_name = 'next'


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]


"""
Getting a token for a registered user
"""


class ObtainTokenView(APIView):
    http_method_names = ['post']
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user = authenticate(request,
                            username=self.request.data.get('username'),
                            password=self.request.data.get('password'))
        if user is not None:
            return Response(str(Token.objects.get(user=user)), 200)
        else:
            return HttpResponse(status=401)
