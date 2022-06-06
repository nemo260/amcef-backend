from django.urls import path
from . import views

urlpatterns = [
    path('posts/get/<int:request_uid>', views.getPosts, name="getPosts"),
    path('posts/add', views.addPost, name="addPost"),
    path('posts/delete/<int:postID>', views.deletePost, name="deletePost"),
    path('posts/update', views.updatePost, name="updatePost"),
]
