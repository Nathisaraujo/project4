from django.db import models


# Collaboration form model from Code Institute Walkthrough - with modifications
class CollaborateRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100, default='Default Title') 
    message = models.TextField()
    posted = models.BooleanField(default=False)
    

    def __str__(self):
        return f"Collaboration request from {self.name}"
