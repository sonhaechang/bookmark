from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return self.site_name+ ' : '+self.url

    class Meta:
        ordering = ['site_name']

    def get_absolute_url(self, *args, **kwargs):
        return reverse('bookmark:detail', args=[str(self.id)])
