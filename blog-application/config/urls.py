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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import RedirectView

from blogs.blog.sitemaps import PostSitemap

from .views import AboutUsView, HomeView

sitemaps = {"posts": PostSitemap}

urlpatterns = [
    # path("", RedirectView.as_view(pattern_name="blog:post_view"), name="register"),
    path("about", AboutUsView.as_view(), name="about_us"),
    path("", HomeView.as_view(), name="home"),
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("management/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("blog/", include("blogs.blog.urls", namespace="blog")),
    path("auth/", include("blogs.authen.urls", namespace="auth")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
