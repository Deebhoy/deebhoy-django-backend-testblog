from django.urls import path
from .views import (BlogListView, 
                    BLogCreateView, 
                    BlogDetailView, 
                    BLogUpdateView, 
                    BlogDeleteView,
                    ProfileBlogListView)

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/new/', 
         BLogCreateView.as_view(),
         name='new_post'),
    
    path('post/<int:pk>/', 
         BlogDetailView.as_view(), 
         name='post_detail'),
    
    path('post/<int:pk>/edit/', 
         BLogUpdateView.as_view(), 
         name='post_edit'),
    
    path('post/<int:pk>/delete/', 
         BlogDeleteView.as_view(), 
         name='post_delete'),

     path('profile/', 
          ProfileBlogListView.as_view(), 
          name='profile')
]