from django.db import models

class Members(models.Model):
    memberName = models.CharField(max_length=255)
    addDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)