from django.urls import path
from django.views.generic import TemplateView

from blog.views import post_views

urlpatterns = [
  path('', post_views.PostView.as_view(), name='home')
]