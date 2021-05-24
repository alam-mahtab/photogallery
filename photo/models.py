from django.db import models

# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    tags = models.ForeignKey(Tags,on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    # def __str__(self):
    #     return self.description, self.image
