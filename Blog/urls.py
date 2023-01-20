from django.urls import path
from .views import BlogView, BlogDetailView

urlpatterns = [
    path('blogs/', BlogView.as_view(), name = "blogs"),
    path('blog/<slug:slug>', BlogDetailView.as_view(), name = "blog_detail"),
]