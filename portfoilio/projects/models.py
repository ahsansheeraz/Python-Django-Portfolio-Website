from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True, null= True)
    live_demo_link = models.URLField(blank=True, null= True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['-created_at']
        verbose_name = "Project"
        verbose_name_plural ="Projects"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('projects:project_detail', kwargs={'slug': self.slug})

