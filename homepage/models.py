from django.db import models

# Create your models here.

# 作品投稿Model
class WorkPost(models.Model):
    post_image = models.ImageField(upload_to="post-images")
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)
    git_url = models.URLField(null=True)
    page_url = models.URLField(null=True)

    class Meta:
        ordering = ["-create_at"]
    
    def __str__(self):
        return self.title 

