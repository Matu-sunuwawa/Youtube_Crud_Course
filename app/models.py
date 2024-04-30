from django.db import models

# Create your models here.

class NoteApp(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title