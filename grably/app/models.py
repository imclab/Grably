from django.db import models

# Create your models here.
class Grabber(models.Model):
   username = models.CharField(max_length = 100) #check for this in the input
   venmo_key = models.CharField(max_length = 100)

class Tasks(models.Model):
    task_id = models.CharField(max_length = 200)
    task_title = models.CharField(max_length = 100)
    task_description = models.CharField(max_length = 1000)
    price = models.IntegerField(default = 0)
    assigner = models.ForeignKey(Grabber)
    executor = models.ForeignKey(Grabber)
    status = models.CharField(max_length = 100)
    location = models.IntegerField()

class Friends(models.Model):
    friender = models.ForeignKey(Grabber)
    friendee = models.ForeignKey(Grabber)
    status = models.CharField(max_length = 100)



