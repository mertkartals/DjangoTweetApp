from django.db import models
from django.contrib.auth.models import User  #kullanıcı modeli
# Create your models here.

class Tweet(models.Model):           #foreign key = yabancı anahtar, modelimiz ise user
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #on delete ile kullanıcı silinince tweet de silinecek
    message = models.CharField(max_length=100)


    def __str__(self):
        return f"Tweet nick:  {self.username}  message: {self.message}"
    