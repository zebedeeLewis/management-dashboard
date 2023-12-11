from django.db import models

class Sample(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ['created']
