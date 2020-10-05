from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=15)
    subtitle = models.CharField(max_length=15)
    tec_img = models.ImageField(verbose_name='技術の写真', upload_to='images/',)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

# Create your models here.
