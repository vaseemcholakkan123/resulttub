from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView , DetailView
from .models import Blog, Category
from django.http import Http404
from django.db.models import Sum



class IndexView(TemplateView):
   extra_context = {"blogs" : Blog.blogObjects.order_by('-views')[:15] ,
                    "categories" : Category.objects.annotate(total_views=Sum('blogs__views')),
                    "total_read" : Blog.blogObjects.aggregate(Sum('views'))['views__sum'] or 0,
                    }
   template_name = 'index.html'


class AboutView(TemplateView):
   extra_context = {"categories" : Category.objects.annotate(total_views=Sum('blogs__views'))}
   template_name = 'about.html'


class BlogView(DetailView):
    model = Blog
    template_name = 'content.html'
    context_object_name = 'blog'
    slug_field = 'slug'
    slug_url_kwarg = 'blog_slug'

    def get_object(self, queryset=None):
        category_slug = self.kwargs.get('category_slug')
        blog_slug = self.kwargs.get('blog_slug')
        
        try:
            category = Category.objects.get(slug=category_slug)
            blog = Blog.objects.get(slug=blog_slug, category=category , status="published")
            blog.views += 1
            blog.save()
            return blog
        except (Category.DoesNotExist, Blog.DoesNotExist):
            raise Http404()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        prev_blog = Blog.blogObjects.filter(created__lt=self.object.created).order_by('-created').first()
        next_blog = Blog.blogObjects.filter(created__gt=self.object.created).order_by('created').first()

        context['prev_blog'] = prev_blog
        context['next_blog'] = next_blog

        return context
    

class DraftView(DetailView):
    model = Blog
    template_name = 'content.html'
    context_object_name = 'blog'
    slug_field = 'slug'
    slug_url_kwarg = 'blog_slug'

