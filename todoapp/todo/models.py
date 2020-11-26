from django.db import models

# Create your models here.
class Todo(models.Model):
    add_date = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=255)

    def __str__(self):
        return str(self.text)
