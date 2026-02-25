from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    image = models.ImageField(upload_to="profile/", null=True, blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    percentage = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.degree

class Skill(models.Model):
    CATEGORY = (
        ('Basic', 'Basic'),
        ('Advanced', 'Advanced'),
        ('Tools', 'Tools'),
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY)

    def __str__(self):
        return self.name

class Training(models.Model):
    organization = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.organization

class Achievement(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
