from django.db import models
from django.utils.text import slugify

# Create your models here.
class WikiArticleTitle(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(default='', blank=True)


    def save(self):
        self.slug = slugify(self.title)
        super(WikiArticleTitle, self).save()

    def __str__(self):
        return '%s' % self.title