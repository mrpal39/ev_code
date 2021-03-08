from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    description =HTMLField()

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})








class feeds(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    description =HTMLField()

    thumbnail = models.ImageField()
    featured = models.BooleanField()
    # content = HTMLField()



    def __str__(self):
        return self.title

class Products(models.Model):
	title       =models.CharField(max_length=100)
	description =models.TextField(blank=True)
	price       =models.DecimalField(decimal_places=2,max_digits=1000)
	summary     =models.TextField(blank=False, null=False)
    # featured    =models.BooleanField()




class MyModel(models.Model):
    ...
    content = HTMLField()