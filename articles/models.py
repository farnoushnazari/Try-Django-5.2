from django.db import models
from django.utils.text import slugify 
from django.db.models.signals import pre_save, post_save

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)

def article_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    print(args, kwargs)
    if instance.slug is None:
        instance.slug = slugify(instance.title)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(*args, **kwargs):
    print('post_save')
    print(args, kwargs)

post_save.connect(article_post_save, sender=Article)