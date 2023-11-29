from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
   path("" , IndexView.as_view(), name="home"),
   path("about/" , AboutView.as_view(), name="about"),
   path('<slug:category_slug>/<slug:blog_slug>/', BlogView.as_view(), name='show_blog'),

   path("drafts/<slug:blog_slug>/", DraftView.as_view(), name='show_draft') # not is sitemap
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
