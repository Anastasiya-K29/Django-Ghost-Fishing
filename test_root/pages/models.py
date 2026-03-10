from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200)
    permalink = models.CharField(max_length=12, unique=True)
    content = models.TextField()
    authors = models.TextField(blank=True)
    references = models.TextField(blank=True)

    def __str__(self):
        return self.title