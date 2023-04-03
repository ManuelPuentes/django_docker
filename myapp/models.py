from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=100, default='')
    creator = models.TextField(max_length=200, default='')
    # popularity = models.IntegerField()
    src = models.TextField(max_length=200, primary_key=True) 
    # src field is the youtube video id 
    thumbnail = models.TextField(max_length=200, default='')
    likes_counter = models.IntegerField(default=0)
    dislikes_counter = models.IntegerField(default=0)




# class Comment(models.Model):
#     creator: models.ForeignKey(User, on_delete=models.CASCADE)
#     content: models.CharField(max_length=300, default='')
#     dest: models.ForeignKey(Video, on_delete=models.CASCADE)


