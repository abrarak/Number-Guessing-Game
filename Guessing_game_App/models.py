from django.db import models

class info(models.Model):
  username = models.CharField(max_length=255)
  usernumber=models.IntegerField()
  systemnumber=models.IntegerField()
  chance=models.IntegerField()
  
