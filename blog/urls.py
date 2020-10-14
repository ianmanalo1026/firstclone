from django.urls import path
from blog import views

urlpatterns = [
    path('home',views.PostListView.as_view(), name='home'),
    path('about', views.AboutView.as_view(),name='about'),
    path('post/<int:blog_id>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:blog_id>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:blog_id>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('draft', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:blog_id>/comment', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:blog_id>/approve', views.comment_approve, name='comment_approve'),
    path('comment/<int:blog_id>/remove', views.comment_remove, name='comment_remove'),
    path('post/<int:blog_id>/publish/', views.post_publish, name='post_publish'),
]
