from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=350)
    post_text = models.TextField
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)
    comment_text = models.CharField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.date_posted} ({self.author})'

class Author(models.Model):
    author = models.CharField(max_length=20)

    class Meta:
        ordering = ['author']
    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '{self.author}'



# Create your models here.
