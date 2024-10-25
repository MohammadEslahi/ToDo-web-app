from django.db import models


class ToDoItem(models.Model):
    text = models.CharField(max_length=20)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.text