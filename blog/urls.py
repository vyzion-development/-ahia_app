from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(template_name='home.html'), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(template_name='user_post'), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(template_name="details_post"), name='post-detail'),
    path('post/new/', PostCreateView.as_view(template_name='form_post.html'), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(template_name='confirm_post.html'), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('assets/Files/<int:pk>',PostDeleteView.as_view(),name='post-delete' ),
    path('search/',views.search,name='search' ),
   
]