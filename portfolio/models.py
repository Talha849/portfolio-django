from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    demo_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(
        max_length=50,
        default='fas fa-code',  # Default icon
        help_text="Font Awesome icon class name (e.g., 'fab fa-python')"
        )
    proficiency = models.PositiveIntegerField(
        default=75,
        help_text="Proficiency level in percentage (0-100)"
        )
    
    def __str__(self):
        return self.name