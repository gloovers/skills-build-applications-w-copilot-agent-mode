from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField()    # in km
    def __str__(self):
        return f"{self.user.username} - {self.type}"

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    duration = models.IntegerField()  # in minutes
    def __str__(self):
        return f"{self.user.username} - {self.description}"

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team.name} - {self.points}"
