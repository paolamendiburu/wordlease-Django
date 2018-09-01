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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.api import MyPostsAPI, PostViewSet, BlogViewSet
from posts.views import HomeView, PostFormView, PostDetailView, BlogListView, BlogPostsView
from users.api import UserViewSet
from users.views import LogoutView, LoginView, signup

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('blogs', BlogViewSet)
router.register('users', UserViewSet, base_name='users')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', BlogListView.as_view(), name="blog-list"),
    path('blogs/<str:username>/<int:pk>', PostDetailView.as_view(), name="post-details"),

    path('', HomeView.as_view(), name="home"),
    path('blogs/<username>/', BlogPostsView.as_view(), name="my-posts"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('signup', signup, name="signup"),
    path('new-post', PostFormView.as_view(), name="create-post"),

    #api

    path('api/v1/', include(router.urls)),
    path('api/v1/my-posts/', MyPostsAPI.as_view(), name="my-posts")


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
