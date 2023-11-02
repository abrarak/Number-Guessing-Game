from django.db import models


class username(models.Model):
  user_name = models.CharField(max_length=255)

class userrangeandchance(models.Model):
    lowerrange=models.IntegerField()
    upperrange=models.IntegerField()
    chance=models.IntegerField()
    systemnumber=models.IntegerField()
  
class usernumber(models.Model):
    usernumber=models.IntegerField()
    