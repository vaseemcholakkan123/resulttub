from django.views.generic import TemplateView , DetailView
from .models import Blog, Category
from django.http import Http404


class IndexView(TemplateView):
   extra_context = {"blogs" : Blog.objects.all()[:5]}
   template_name = 'index.html'

    
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
            blog = Blog.objects.get(slug=blog_slug, category=category)
            return blog
        except (Category.DoesNotExist, Blog.DoesNotExist):
            raise Http404()