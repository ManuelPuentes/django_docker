from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)

class Video(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    popularity = models.IntegerField()
    likes_counter = models.IntegerField()
    url = models.TextField(2000)
    dislikes_counter = models.IntegerField()

class Comment(models.Model):
    creator: models.ForeignKey(User, on_delete=models.CASCADE)
    content: models.CharField(max_length=300)
    dest: models.ForeignKey(Video, on_delete=models.CASCADE)


