from django.db import models

# Create your models here.
class Gallery(models.Model):
    # u can check field in the helpdocument
    description = models.CharField(default = "此处为作品的描述", max_length = 100)
    img = models.ImageField(default = "default.png" , upload_to = 'images/')
    title = models.CharField(default = "作品标题", max_length = 50)
    
    def __str__(self):
        return  self.title

