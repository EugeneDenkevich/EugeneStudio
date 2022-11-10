from django.db import models


class Task(models.Model):

    title = models.CharField('Title', max_length=150, blank=False)
    description = models.TextField('Description', max_length=500, blank=False)
    add_data = models.DateTimeField()

    def __str__(self):
        return self.title