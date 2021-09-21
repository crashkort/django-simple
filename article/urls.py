from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name = "article/index.html"), name='index'),
]







