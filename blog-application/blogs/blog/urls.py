from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post_view"),
    path("tag/<slug:tag_slug>/", views.post_list, name="post_tag_view"),
    path("create", views.PostCreateView.as_view(), name="post_create"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path("check-prime/<int:numb>/", views.PrimeView.as_view(), name="check_prime"),
    path("<int:post_id>/share/", views.post_share, name="post_share"),
    path("feed", LatestPostsFeed(), name="post_feed"),
    path("search", views.post_search, name="post_search"),
]
