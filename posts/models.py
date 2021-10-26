from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)
    
    def __str__(self):
        return  f'{self.author} | {self.title}'

    def get_absolute_url(self): 
        return reverse('post_detail', args=[str(self.id)])  

    def number_of_likes(self):
        return self.likes.count()      

    class Meta:
        ordering = ('-created_at',)


    