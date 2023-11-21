from django.db import models
from django.utils.text import slugify



class Category(models.Model):
   title = models.CharField(max_length=50)
   slug = models.SlugField(max_length=255, unique=True, blank=True)


   def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.title)
      super().save(*args, **kwargs)


   def __str__(self):
      return self.title



class Blog(models.Model):
   title = models.CharField(max_length=255)
   context = models.TextField()
   conclusion = models.TextField()
   category = models.OneToOneField(Category , on_delete=models.CASCADE)
   seo_description = models.TextField()
   seo_keywords = models.TextField()
   slug = models.SlugField(max_length=255, unique=True, blank=True)


   def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.title)
      super().save(*args, **kwargs)

   def __str__(self):
        return self.title



class Thread(models.Model):
   blog = models.ForeignKey(Blog , on_delete=models.CASCADE , related_name='threads')
   title = models.CharField(max_length=255, blank=False)
   context = models.TextField()
   related_image = models.ImageField(upload_to="media/" , blank=True, null=True)
   code = models.TextField(blank=True, null=True)
   tail_text = models.TextField(blank=True, null=True)


   def __str__(self):
        return self.title + " " + self.blog.title[:10] + "..."


