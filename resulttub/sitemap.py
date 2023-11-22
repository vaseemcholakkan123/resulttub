from django.contrib.sitemaps import Sitemap
from main.models import Blog
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 1
    changefreq = 'daily'

    def items(self):
        sitemaps_list = ['main:home',]
        return sitemaps_list

    def location(self, item):
        return reverse(item)
         


class ResultTubSitemap(Sitemap):
   changefreq = "weekly"
   priority = 0.8

   def items(self):
      return Blog.objects.all()

   def lastmod(self, obj):
      return obj.created
   
   def location(self, obj):
      return reverse('main:show_blog', kwargs={'category_slug': obj.category.slug, 'blog_slug': obj.slug})