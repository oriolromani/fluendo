from django.db import models


class ToDoItem(models.Model):
    name = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
