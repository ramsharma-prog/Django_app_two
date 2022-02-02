from django.urls import path
from . import views


# POSTS URLS

app_name = 'posts'

urlpatterns = [
    path('post_list/', views.PostListView.as_view(), name='post_list'),
    path('user/<str:username>/', views.UserPostListView.as_view(), name='user_posts'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('details/<int:pk>/', views.PostDetailView.as_view(), name='post_details'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('<str:category>/', views.CategoryPostListView.as_view(),
         name='category_posts'),
    path('posts/<int:pk>/comment/', views.add_comment_to_post,
         name='post_comment_list'),
    path('delete_comment/<int:pk>/',
         views.CommentDeleteView.as_view(), name='delete_comment'),
    path('comment/<int:pk>/reply/', views.reply_to_comment, name='reply'),


]
