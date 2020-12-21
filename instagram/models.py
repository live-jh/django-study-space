from django.db import models


# Create your models here.
class Post(models.Model):
    message = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    # java의 toString과 같은 역할
    def __str__(self):
        # return f"Custom Post object ({self.id}-{self.message})"
        return self.message
