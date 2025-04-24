from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)  

    def __str__(self):
        return self.name

class TrainingContent(models.Model):
    title = models.CharField(max_length=100)  
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    video_path = models.CharField(max_length=255)  
    demo_link = models.URLField(blank=True)  
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title