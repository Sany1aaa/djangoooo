from django.urls import path 
from .views import post_list, post_detail, create_post, update_post, delete_post, comment_list, add_comment

urlpatterns=[
    path('post_list/', post_list, name="post_list"), 
    path('post_details/<int:id>', post_detail, name='post_detail'), 
    path('post_create/', create_post, name='post_create'), 
    path('post_update/<int:id>', update_post, name='post_update'), 
    path('post_delete/<int:id>', delete_post, name='post_delete'), 
    path('post_detail/comment_list/<int:post_id>', comment_list, name="comment_list"), 
    path('post_detail/add_comment/<int:post_id>', add_comment, name="add_comment")
]