from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(blank=False, max_length=100)
    def __unicode__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(blank=False, max_length=100)
    course = models.ForeignKey(Course)
    def __unicode__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(blank=False, max_length=100)
    lesson= models.ForeignKey(Lesson)
    def __unicode__(self):
        return self.title