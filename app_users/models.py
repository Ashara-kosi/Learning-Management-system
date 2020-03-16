from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pix', default='default.jpg')
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta():
        ordering = ["-created_on"]

    def __str__(self):
        return f"Profile for {self.user.username}"
