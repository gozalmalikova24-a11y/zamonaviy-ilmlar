from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class LessonProgress(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='progress', on_delete=models.CASCADE)
    user = models.CharField(max_length=100)  # Assuming there's a User model you want to link with
    completed = models.BooleanField(default=False)
    progress_percentage = models.FloatField(default=0.0)
    updated_at = models.DateTimeField(auto_now=True)