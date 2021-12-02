from django.db import models

# Create your models here.


class UserProfile(models.Model):
    #image = models.FileField(upload_to="images") # ulooad_to create a file inside the file we added in the settings.
    image = models.ImageField(upload_to="images")

    def __str__(self) :
        return f"{self.image}"