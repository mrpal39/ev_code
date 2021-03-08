from django.db import models
from blog.models import Post
# Creating a comment systems


class Comment(models.Model):
    post = models.ForeignKey(Post,
                   on_delete=models.CASCADE,
                   related_name='comments')
    name=models.CharField(max_length=200)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('created',)

    def __str__(self):
        return f'comment by {self.name}on{self.post}'   
    


# 
# 