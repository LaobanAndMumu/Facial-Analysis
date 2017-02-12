from django.db import models

class Analysis(models.Model):
    different = models.CharField(max_length=100)
    attribute = models.CharField(max_length=100)
    description = models.TextField()



