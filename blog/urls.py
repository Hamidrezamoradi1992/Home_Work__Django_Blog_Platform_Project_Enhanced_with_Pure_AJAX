from django.urls import path

from blog import views

urlpatterns=[
    path('',views.index,name='home'),
    path('api/',views.Author_GET_all_view,name='get_post'),
    path('api/author/<int:pk>',views.Author_update_delete_detail_view,name='update_delete_view_author'),
    path('api/author',views.create_author,name='create_author'),
    path('api/author/post/<int:pk>',views.pst_view,name='post_author'),
    path('api/author/post/create/<int:pk>',views.create_post,name='post_create'),
    path('api/author/delet/<int:pk>',views.post_update_delete_detail_view,name='update_delete_view_post'),
]