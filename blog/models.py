from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50, blank = True)
    date_time = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']