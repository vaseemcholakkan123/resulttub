from django.contrib import admin
from django.urls import path , include , re_path
from django.views.generic import TemplateView
from .sitemap import ResultTubSitemap, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap


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
