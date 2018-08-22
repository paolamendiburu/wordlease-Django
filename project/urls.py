"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts.views import HomeView, PostDeitalView, PostFormView, MyPostsView
from users.api import UsersAPI, UserDetailAPI
from users.views import LogoutView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/<int:pk>', PostDeitalView.as_view(), name="post-detail"),
    path('', HomeView.as_view(), name="home"),
    path('my-posts', MyPostsView.as_view(), name="my-posts"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('new-post', PostFormView.as_view(), name="create-post"),

    #api
    path('api/v1/users/', UsersAPI.as_view(), name="users-api"),
    path('api/v1/users/<int:pk>', UserDetailAPI.as_view(), name="userdetail-api")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
