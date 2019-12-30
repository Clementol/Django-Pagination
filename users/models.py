from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    first_name = models.CharField( max_length=50)
    user_email = models.CharField( max_length=50)

    def __str__(self):
        return self.user_name + ' - ' + self.first_name + ' - ' +  self.user_email 
    
