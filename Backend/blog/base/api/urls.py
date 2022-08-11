from django.urls import path
from base.api import views as api_views

urlpatterns = [
    path('blogs/',api_views.BlogListCreateAPIView.as_view(), name='blog-list'),
    path('blogers/',api_views.BlogerListCreateAPIView.as_view(), name='bloger-list'),
    path('blogs/<int:pk>', api_views.BlogDetailAPIView.as_view(), name='blog-detay'),
]


#FUNCTION BASED VIEWS
# urlpatterns = [
#     path('blogs/',api_views.blog_list_create_api_view, name='blog-list'),
#     path('blogs/<int:pk>', api_views.blog_detail_api_view, name='blog-detay'),
# ]