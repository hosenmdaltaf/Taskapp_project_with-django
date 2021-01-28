from django.db import models

class Task(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    headline = models.CharField(max_length=200)
    # content = models.TextField()
   
    def __str__(self):
        return self.headline
