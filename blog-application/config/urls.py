"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.sitemaps.views import sitemap
from blogs.blog.sitemaps import PostSitemap
from .views import HomeView, AboutUsView

sitemaps = {"posts": PostSitemap}

urlpatterns = [
    # path("", RedirectView.as_view(pattern_name="blog:post_view"), name="register"),
    path("about", AboutUsView.as_view(), name="about_us"),
    path("", HomeView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("blog/", include("blogs.blog.urls", namespace="blog")),
    path("auth/", include("blogs.auth.urls", namespace="auth")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
