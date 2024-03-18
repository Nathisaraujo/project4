from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))


# Post model from Code Institute Walkthrough - with modifications
class Post(models.Model):
    """
    Model for blog posts.

    This model represents all the blog posts. It includes fields for
    the post title, slug, author, content, creation date, status, excerpt,
    update date, liked votes, silly votes, more information votes, and approval
    status. It also includes property methods to calculate the number of votes
    requests for each post.

    **Fields**
    - title (CharField) - title of the post
    - slug (SlugField) - slug of the post
    - author (ForeignKey to User) - author of the post
    - content (TextField) - Post text
    - created_on (DateTimeField) - when the post was created
    - status (IntegerField with choices) - if it's published or a draft
    - excerpt (TextField) - Text summarizing the post content
    - updated_on (DateTimeField) - When the post was created
    - liked (ManyToManyField to User) - button to vote as not silly
    - like_count (PositiveIntegerField) - not silly votes counter
    - sillied (ManyToManyField to User) - button to vote as silly
    - silly_count (PositiveIntegerField) - silly votes counter
    - more (ManyToManyField to User) - button to vote as more information
    - more_count (PositiveIntegerField) - more information votes counter
    - approved (BooleanField) - admin field to mark post as approved

    **Property Methods**
    - num_likes: Returns the number of not silly votes for the post.
    - num_silly: Returns the number of silly votes for the post.
    - num_more: Returns the number of more information votes for the post.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(max_length=500, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    # My objects
    liked = models.ManyToManyField(
        User, default=None, related_name='liked_posts', blank=True
    )
    like_count = models.PositiveIntegerField(default=0)
    sillied = models.ManyToManyField(
        User, default=None, related_name='silly_posts', blank=True
    )
    silly_count = models.PositiveIntegerField(default=0)
    more = models.ManyToManyField(User, related_name='more_info', blank=True)
    more_count = models.PositiveIntegerField(default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on", "author"]

    def __str__(self):
        return f"{self.title} | sent by {self.author} "

    # My property methods
    @property
    def num_likes(self):
        return self.liked.count()

    def num_silly(self):
        return self.sillied.count()

    def num_more(self):
        return self.sillied.count()

# Users comments model from Code Institute Walkthrough


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.s
    """
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
