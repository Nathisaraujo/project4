from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
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
    like_count = models.IntegerField(default=0)


    class Meta:
        ordering = ["-created_on", "author"]


    def __str__(self):
        return f"{self.title} | sent by {self.author} "

    @property
    def num_likes(self):
        return self.liked.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-created_on"]

        
    def __str__(self):
        return f"{self.body} by {self.author}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post)
    
    def save(self, *args, **kwargs):
        super(Like, self).save(*args, **kwargs)
        self.post.like_count = Like.objects.filter(post=self.post).count()
        self.post.save()
