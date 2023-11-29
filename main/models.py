from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model



class Category(models.Model):
   title = models.CharField(max_length=50)
   slug = models.SlugField(max_length=255, unique=True, blank=True)
   accent = models.CharField(max_length=20, blank=True, default="#04baf6")


   def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.title)
      super().save(*args, **kwargs)


   def __str__(self):
      return self.title
   
   class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"



class Blog(models.Model):
   class BlogObjects(models.Manager):
      def get_queryset(self):
         return super().get_queryset().filter(status="published")
      
   VISIBILITY = (("published", "published"), ("draft", "draft"))
   ALLOW_COMMENTS = (("allow", "allow"), ("disallow", "disallow"))

   title = models.CharField(max_length=255)
   author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE, related_name="author")
   status = models.CharField(max_length=30, choices=VISIBILITY, default="draft")
   allow_comments = models.CharField(
        max_length=30, choices=ALLOW_COMMENTS, default="disallow"
    )
   context = models.TextField()
   conclusion = models.TextField()
   category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name="blogs")
   seo_description = models.TextField()
   seo_keywords = models.TextField()
   slug = models.SlugField(max_length=255, unique=True, blank=True)
   views = models.PositiveBigIntegerField(default=121)
   created = models.DateTimeField(auto_now_add=True)

   objects = models.Manager()
   blogObjects = BlogObjects()


   def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.title)
      super().save(*args, **kwargs)

   def __str__(self):
        return self.title

   @staticmethod
   def get_top_viewed_blogs():
      return Blog.blogObjects.order_by('-views')[:10]
   
   class Meta:
      ordering = ("-created",)
      verbose_name = "Blog"
      verbose_name_plural = "Blogs" 



class Thread(models.Model):
   blog = models.ForeignKey(Blog , on_delete=models.CASCADE , related_name='threads')
   title = models.CharField(max_length=255, blank=False)
   context = models.TextField()
   related_image = models.ImageField(upload_to="media/" , blank=True, null=True)
   thread_link = models.CharField(max_length=255,blank=True)
   code = models.TextField(blank=True, null=True)
   tail_text = models.TextField(blank=True, null=True)
   rm_counter = models.BooleanField(default=False, null=True)


   def __str__(self):
        return self.title + " : " + self.blog.title[:30] + "..."


