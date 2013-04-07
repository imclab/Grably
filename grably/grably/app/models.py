from django.db import models

# Create your models here.
class Grabber(models.Model):
   username = models.CharField(max_length = 100) #check for this in the input
   venmo_key = models.CharField(max_length = 100)
   twitter = models.CharField(max_length = 100, blank = True, null=True)#tweeter handle

class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length = 100)
    task_description = models.CharField(max_length = 1000)
    date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits = 4, default = 0.00, decimal_places = 2)
    assigner = models.ForeignKey(Grabber, related_name="assigner_id")
    executor = models.ForeignKey(Grabber, related_name="executor_id")
    status = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)

class Friends(models.Model):
    friender = models.ForeignKey(Grabber, related_name="friender_id")
    friendee = models.ForeignKey(Grabber, related_name="friendee_id")
    status = models.CharField(max_length = 100)

