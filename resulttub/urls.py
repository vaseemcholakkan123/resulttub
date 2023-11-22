from django.contrib import admin
from django.urls import path , include , re_path
from django.views.generic import TemplateView
from .sitemap import ResultTubSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from django.conf.urls import handler404
from django.shortcuts import render
from main.models import Category
from django.db.models import Sum


def error_404_view(request, exception):
    return render(request, '404.html', status=404 , context={"categories" : Category.objects.annotate(total_views=Sum('blogs__views'))})

handler404 = error_404_view

sitemaps = {
    'sitemaps': ResultTubSitemap, 'flatpages': StaticViewSitemap,
}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("" , include("main.urls")),

    
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name='extras/robots.txt', content_type='text/plain')),
    # re_path(r'^ads\.txt$', TemplateView.as_view(template_name='extras/ads.txt', content_type='text/plain')),
    re_path(r'^sitemap\.xml$', sitemap, {
            'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
