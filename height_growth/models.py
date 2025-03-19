from django.db import models

class DietPlan(models.Model):
    day = models.CharField(max_length=20)
    Morning = models.TextField()
    breakfast = models.TextField()
    lunch = models.TextField()
    dinner = models.TextField()

    def __str__(self):
        return self.day

class Exercise(models.Model):
    day = models.ForeignKey(DietPlan, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Animation(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='animations')
    youtube_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Animation for {self.exercise.name}"