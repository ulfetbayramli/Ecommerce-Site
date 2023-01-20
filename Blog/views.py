from django.shortcuts import redirect
from django.db.models import Q 
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import CommentForm

class BlogView(ListView):
    template_name = "blog.html"
    model = Blog
    context_object_name = "posts"

    def get_queryset(self):
        category = self.request.GET.get("category")
        author = self.request.GET.get("author")
        if category:
            self.queryset = Blog.objects.filter(category__name = category).order_by("-date").all()[:4]
        elif author:
            self.queryset = Blog.objects.filter(author__author_slug = author).order_by("-date").all()[:4]
        else:
            self.queryset = Blog.objects.order_by("-date").all()[:4]
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['p_posts'] = Blog.objects.order_by("-read_count").all()[:4]
        context['categories'] = Category.objects.all()
        context['authors'] = Author.objects.all()
        return context

class BlogDetailView(DetailView, CreateView):
    template_name = 'blog_detail.html'
    slug_url_kwarg = 'slug'
    model = Blog
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        blog = Blog.objects.get(slug=self.kwargs.get("slug"))
        blog.read_count += 1
        blog.save()
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return Blog.objects.get(slug=self.kwargs.get("slug"))

    def form_valid(self, form):
        form.instance.blog = self.get_object()
        form.instance.save()
        return redirect('blog_detail', slug=self.kwargs.get("slug"))

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['r_blogs'] = Blog.objects.filter(Q(category = kwargs['object'].category), ~Q(slug = self.kwargs.get("slug"))).all()[:5]
        context['p_posts'] = Blog.objects.order_by("-read_count").all()[:4]
        context['categories'] = Category.objects.all()
        context['comments'] = Comment.objects.filter(blog__slug = self.kwargs.get("slug")).order_by("-date").all()[:5]
        return context
    