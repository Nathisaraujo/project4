from django.db import models


# Collaboration form model from Code Institute Walkthrough - with modifications
class CollaborateRequest(models.Model):
    """
    Model to store collaboration requests.

    This model represents a collaboration request submitted by a user,
    including their name, email, title, message, and a flag
    indicating whether the request has been posted.

    **Fields**
    - name: name of the person sending the stories for admin control
    - email: email of the story sender
    - title: title of the post
    - message: text content of the post
    - posted: admin can mark the story as posted

    **Methods**
    - __str__: Returns a string representation of the collaboration request.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100, default='Default Title')
    message = models.TextField()
    posted = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the collaboration request.

        This method returns the name of the person submitting the collaboration
        request along with the prefix "Collaboration request from".

        **Returns**
        - str: String representation of the collaboration request.
        """
        return f"Collaboration request from {self.name}"
