from django.db import models
import random


class Tweet(models.Model):
    # id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta():
        ordering = ['-id']

    def __str__(self):
        return self.content
        
    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'likes': random.randint(0,50)
        }


