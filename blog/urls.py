from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreateView


app_name = 'blog'

urlpatterns = [
    path('blog_list', BlogListView.as_view(template_name='blog/blog_list.html'), name='blog_list'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(template_name='blog/blog_detail.html'), name='blog_detail'),
    path('blog_create', BlogCreateView.as_view(template_name='blog/blog_form.html'), name='blog_create')
]