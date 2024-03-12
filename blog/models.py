from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


# Post model with each post details
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(User, default=None, related_name='liked_posts', blank=True)
    like_count = models.PositiveIntegerField(default=0)
    sillied = models.ManyToManyField(User, default=None, related_name='silly_posts', blank=True)
    silly_count = models.PositiveIntegerField(default=0)
    more = models.ManyToManyField(User, related_name='more_info')
    more_count = models.PositiveIntegerField(default=0)
    approved = models.BooleanField(default=False)


    class Meta:
        ordering = ["-created_on", "author"]


    def __str__(self):
        return f"{self.title} | sent by {self.author} "

    @property
    def num_likes(self):
        return self.liked.count()
    def num_silly(self):
        return self.sillied.count()
    def num_more(self):
        return self.sillied.count()


# Users comments model
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField(max_length=500)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-created_on"]

        
    def __str__(self):
        return f"{self.body} by {self.author}"
