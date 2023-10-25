from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", TemplateView.as_view(template_name="web/about.html"),name="about"),
    path("work/", TemplateView.as_view(template_name="web/work.html"),name="work"),
    path("blog/", TemplateView.as_view(template_name="web/blog.html"),name="blog"),
    path("contact/", views.contact, name="contact"),
]