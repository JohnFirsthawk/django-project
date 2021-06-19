from django.db import models

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=512)

    class Meta:
        verbose_name_plural = 'posts'