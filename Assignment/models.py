from django.db import models

# Create your models here.
class SaveForms(models.Model):
    name = models.CharField(max_length=225, null=True)
    email = models.CharField(max_length=225, null=True)
    phone = models.IntegerField(null=True)
    desc = models.TextField(null=True)
    
    def __str__(self):
        return f"{self.name}"
