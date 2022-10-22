from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

# Create your views here.


class HomeView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self):
        return reverse("blog:post_view")


class AboutUsView(TemplateView):
    template_name: str = "aboutus.html"
