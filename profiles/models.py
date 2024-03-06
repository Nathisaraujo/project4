from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class UsersPostRequest(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default='Default Title') 
    message = models.TextField()
    excerpt = models.TextField(max_length=200, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"

    def to_post(self):
        """
        Método para criar um objeto Post a partir deste objeto UsersPostRequest aprovado.
        Retorna None se o UsersPostRequest não estiver aprovado.
        """
        if self.approved:
            # Criar um novo objeto Post com base nas informações de UsersPostRequest
            post = Post(
                title=self.title,
                content=self.message,
                excerpt=self.excerpt,
                created_on=self.created_on,
                status=1,  # Defina o status como publicado
                # Você pode precisar ajustar o autor dependendo da sua lógica de usuário
                author=self.author,  # Suponho que você tenha um campo author em UsersPostRequest
            )
            post.save()  # Salvar o novo post no banco de dados
            return post
        return None