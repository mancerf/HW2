from blog.models import Blog
from django.shortcuts import render, get_object_or_404
from .forms import BlogForm

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy, reverse


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"

    def get_object(self, queryset=None):
        blog = super().get_object(queryset)
        blog.views_count += 1
        blog.save()
        return blog


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")