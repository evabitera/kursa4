from django.urls import reverse_lazy
from django.views import generic

from .form import BlogForm
from .models import Blog


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog/blog_list.html'


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()

        return self.object


class BlogCreateView(generic.CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')
    extra_context = {
        'title': 'Создание блога'
    }
