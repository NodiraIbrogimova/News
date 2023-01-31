from django.db import models

class Article(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # publishedAt = models.DateTimeField()

    def __str__(self):
        return self.title