from django.db import models

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100, default='Default Title') 
    message = models.TextField()
    posted = models.BooleanField(default=False)
    

    def __str__(self):
        return f"Collaboration request from {self.name}"
