from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    media_content = models.ImageField(null=True, blank=True, upload_to="news/%Y/%m/%d")

    def __str__(self):
        return self.title

    def url(self):
        return reverse("blog:news_detail", args=[self.id])

    class Meta:
        ordering = ["updated"]
