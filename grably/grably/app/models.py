from django.db import models

# Create your models here.
class Grabber(models.Model):
   username = models.CharField(max_length = 100) #check for this in the input
   venmo_key = models.CharField(max_length = 100)

class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length = 100)
    task_description = models.CharField(max_length = 1000)
    date = models.DateField(auto_now_add=True)
    price = models.IntegerField(default = 0)
    assigner = models.ForeignKey(Grabber, related_name="assigner_id")
    executor = models.ForeignKey(Grabber, related_name="executor_id")
    status = models.CharField(max_length = 100)
    location = models.IntegerField()

class Friends(models.Model):
    friender = models.ForeignKey(Grabber, related_name="friender_id")
    friendee = models.ForeignKey(Grabber, related_name="friendee_id")
    status = models.CharField(max_length = 100)



