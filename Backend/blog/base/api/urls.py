from django.urls import path
from base.api import views as api_views

urlpatterns = [
    path('blogs/',api_views.blog_list_create_api_view,name='blog-list'),
]