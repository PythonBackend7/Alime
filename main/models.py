from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Gallery(TimeStamp):
    image_link = models.ImageField(upload_to='gallery')
    image = models.ImageField(upload_to='gallery')


class About(TimeStamp):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='about')
    video_link = models.ImageField(upload_to='abouts')
    description = models.TextField()

    def __str__(self):
        return self.title


class Our_Offer(TimeStamp):
    icon = models.ImageField(upload_to='about')
    title = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.title


class Social_media(TimeStamp):
    link = models.URLField()


class Team(TimeStamp):
    image = models.ImageField(upload_to='team')
    name = models.CharField(max_length=212)
    occupation = models.CharField(max_length=212)
    s_media = models.ManyToManyField(Social_media, null=True, blank=True)

    def __str__(self):
        return self.name


class Instagram(TimeStamp):
    image = models.ImageField('instagram')
    link = models.URLField()


class Category(TimeStamp):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Tag(TimeStamp):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Article(TimeStamp):
    title = models.CharField(max_length=212)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body1 = models.TextField()
    quote = models.TextField()
    quote_author = models.CharField(max_length=212)
    body2 = models.TextField()
    image = models.ImageField(upload_to='posts')
    categry = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(TimeStamp):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='comments')
    message = models.TextField()

    def __str__(self):
        return self.name
