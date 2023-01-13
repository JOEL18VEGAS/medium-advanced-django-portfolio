from django.db import models

# Create your models here.
class Project(models.Model):
    
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects')
    link = models.URLField(null=True, blank=True)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        
        db_table = 'project'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-created']

        def __str__(self):
            return self.title

