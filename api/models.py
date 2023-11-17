from django.db import models

def file_location(instance, filename, **kwargs):
    file_path = f"article/{instance.title}-{filename}"
    return file_path
    
class Image(models.Model):
    # title = models.CharField(max_length=255)
    # content = models.TextField(max_length=5000, null=False, blank=False)
    image = models.ImageField(upload_to="images/", null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")
    def __str__(self):
        return self.title
    
class ClassifiedImage(models.Model):
    category = models.CharField(max_length=255),
    # score = models.DecimalField(max_digits=4, decimal_places=1)
    score = models.CharField(max_length=5),
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")
    def __str__(self):
        return self.category
    


