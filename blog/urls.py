from django.urls import path, include
from blog.views import (
    BlogCommentCreateView, BlogCommentDeleteView, BlogCommentDetailView, BlogCommentListView, BlogCommentUpdateView, BlogCreateView, BlogImageDeleteView, BlogListView,
    BlogDetailView, BlogUpdateView, BlogDeleteView
)

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('list/', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/detail/', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('<int:pk>/comment/create/', BlogCommentCreateView.as_view(), name='blog_comment_create'),
    path('<int:pk>/comment/list/', BlogCommentListView.as_view(), name='blog_comment_list'),
    path('<int:pk>/comment/<int:blog_comment_id>/detail/', BlogCommentDetailView.as_view(), name='blog_comment_detail'),
    path('<int:pk>/comment/<int:blog_comment_id>/update/', BlogCommentUpdateView.as_view(), name='blog_comment_update'),
    path('<int:pk>/comment/<int:blog_comment_id>/delete/', BlogCommentDeleteView.as_view(), name='blog_comment_delete'),
    path('<int:pk>/image/<int:blog_image_id>/delete/', BlogImageDeleteView.as_view(), name='blog_image_delete'),

]

