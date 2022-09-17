"""apidemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI, Schema

api = NinjaAPI()


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


@api.get('/hello')
def hello(request, name='world'):
    return f"Hello {name}"


@api.get('/math/{a}and{b}')
def math(request, a: int, b: int):
    return {'add': a + b, 'multiply': a * b}


class HelloSchema(Schema):
    name: str = "world"


@api.post('/hello-post')
def hello_post(request, data: HelloSchema):
    return f"Hello {data.name}"


class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = ''
    first_name: str = ''
    last_name: str = ''


class Error(Schema):
    message: str


# AttributeError: 'SessionStore' object has no attribute '_session_cache' ???
@api.get('/me', response={200: UserSchema, 403: Error})
def me(request):
    if not request.user.is_authenticated:
        return 403, {'message': 'Please sign in first.'}
    return request.user


urlpatterns = [path('admin/', admin.site.urls), path('api/', api.urls)]
