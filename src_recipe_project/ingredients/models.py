from django.db import models

# Create Ingredients model
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    pic = models.ImageField(upload_to='ingredients', default='no_picture.jpg')

    def __str__(self):
        return self.name
