from django.db import models

# Create your models here.
class WikiArticle(models.Model):

    content = models.TextField()
    author = models.CharField(max_length=255)
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self):
        super(WikiArticle, self).save()