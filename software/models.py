from django.db import models  # type: ignore


class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title
