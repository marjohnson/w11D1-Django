from django.db import models

class Skill(models.Model):
    skillName = models.CharField(max_length=45)
    addedSkill = models.DateTimeField(auto_now_add=True)
    updatedSkill = models.DateTimeField(auto_now=True)