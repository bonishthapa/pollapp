from django.db import models

# Create your models here.

class Polldata(models.Model):
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option1_count = models.IntegerField(default=0)
    option2_count = models.IntegerField(default=0)
    option3_count = models.IntegerField(default=0)

    def __str__(self):
        return self.question

    def total(self):
        return self.option1_count + self.option2_count + self.option3_count    