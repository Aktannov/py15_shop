# MVC - Model View Control
# Model - связь с базой данных(models.py)
# View - представление данных (serializer.py)
# Controler - обработчик запросов которые приходят от клиентов(view.py)
# API(Application Programming Interface) - итерфейс для взоимодействия программ
# RESTful API - API отвечающий стилб REST
# REST - набор правил для построения приложения
# 1. модель клиента - сервер
# 2. отсутсвует состояние клиентов (на сервере не хронятся данные о том, зологинин пользователь или нет)
# GET api/v1/products - список
# POST api/v1/products - сщздание
# 3. кеширование
# 4. единообразие интерфейса
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView

from account.models import User
from account.serializer import RegisterSerializer, ActivationSerializer, LoginSerializer, ChangePasswordSerializer, \
    ForgotPasswordSerializer, ForgotPasswordCompliteSerializer, DeiSerializer


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.create()
            message = f'Вы успешно зарегестрировались\nВам отправлено письмо активации'
            return Response(message, status=201)


class ActivationView(APIView):
    def post(self, requests):
        data = requests.data
        serializer = ActivationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Ваш акккаунт успешно активироан')


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, requests):
        user = requests.user
        Token.objects.filter(user=user).delete()
        return Response('Вы успешно разлогинились')


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.data
        serializer = ChangePasswordSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.set_new_pass()
        return Response('Пароль успешно обнавлен')


class ForgotPasswordView(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordSerializer(data=data)
        #       проверка данных
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('Вам отправлено письмо для восстановления пароля')


class ForgotPasswordComplite(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordCompliteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_pass()
        return Response('Пароль успешно обнавлен')


class Ret(APIView):
    def post(self, request):
        data = request.data
        serializer = DeiSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response('Олень ты зарегался')



def test_view(request):
    return HttpResponse('Hello world')
