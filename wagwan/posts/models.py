from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from accounts.models import Profile
import misaka
from django.shortcuts import render

# POST MODELS


# ------------------------TAGS & CATEGORY MODELS-------------------------------#
class Tag(models.Model):
    """ To be worked  """
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """ To be worked  """
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

# ------------------------POST  MODEL-------------------------------#


class Post(models.Model):

    CHOICES = (
        ('celebrate', 'celebrate'),
        ('planning', 'planning'),
        ('outdoor', 'outdoor'),
        ('holidays', 'holidays'),
        ('festivals', 'festivals'),
        ('movies', 'movies'),
        ('shopping', 'shopping'),
        ('laptop', 'laptop'),
        ('data', 'data'),
        ('science', 'science'),
        ('summers', 'summers'),
        ('medical', 'medical'),
        ('art', 'art'),

    )

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               default="")
    title = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    category = models.CharField(max_length=100,
                                null=True, choices=CHOICES)
    tags = models.ManyToManyField(Tag)

    class Meta:
        """ Meta class to change the configuration,
        ordering by the given attribute"""
        ordering = ['-date_posted']

    def get_absolute_url(self):
        """ Reverse the Post object to the url once action
        has been taken with primary key to direct back to the
        same post """
        return reverse('posts:post_list')

    def __str__(self):
        return self.title

# ------------------------COMMENT MODEL-------------------------------#


class Comment(models.Model):
    """ comments for Post model  """

    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE,
                                     related_name='comment_for_post', null=True, default='')
    comment_text = models.TextField(null=True)
    date_posted = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        """ Reverse the Comment to the url once action
        has been taken with primary key to direct back to details page """
        return reverse('posts:post_details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.comment_text

# ------------------------ REPLY TO COMMENTS MODEL-------------------------------#


class Reply(models.Model):
    """ add reply to commnets """
    reply_comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, null=True, default='',
        related_name='comment_reply')
    reply_text = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reply_text
