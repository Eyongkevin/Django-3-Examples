from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import RedirectView, TemplateView

# Create your views here.


class HomeView(RedirectView):
    def get_redirect_url(self):
        return reverse("blog:post_view")


class AboutUsView(TemplateView):
    template_name: str = "aboutus.html"
