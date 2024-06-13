from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.content} {self.is_done} {self.created_at}'
