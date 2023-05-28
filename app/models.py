from django.db import models

# Create your models here.

class csvs(models.Model):
    state=models.CharField(max_length=100)
    year=models.IntegerField(max_length=4)
    men=models.IntegerField()
    women=models.IntegerField()
    men_child=models.IntegerField()
    women_child=models.IntegerField()

    def __str__(self):
        return self.state
