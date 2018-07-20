from django.db import models


class About(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=35)

    def __str__(self):
        return self.firstName

    def __str__(self):
        return self.lastName

    def __str__(self):
        return self.address

    def __str__(self):
        return self.mobile

    def __str__(self):
        return self.email


class Experience(models.Model):
    position = models.CharField(max_length=30)
    companyName = models.CharField(max_length=40)
    aboutJob = models.CharField(max_length=500)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.position

    def __str__(self):
        return self.companyName

    def __str__(self):
        return self.aboutJob

    def __str__(self):
        return self.duration


class Education(models.Model):
    institution = models.CharField(max_length=50)
    degree = models.CharField(max_length=40)
    subject = models.CharField(max_length=50)
    averageGrade = models.CharField(max_length=20)
    graduateYear = models.CharField(max_length=40)

    def __str__(self):
        return self.institution

    def __str__(self):
        return self.degree

    def __str__(self):
        return self.subject

    def __str__(self):
        return self.averageGrade

    def __str__(self):
        return self.graduateYear


class Project(models.Model):
    projectName = models.CharField(max_length=50)
    usedLanguage = models.CharField(max_length=20)
    aboutProject = models.CharField(max_length=500)

    def __str__(self):
        return self.projectName

    def __str__(self):
        return self.usedLanguage

    def __str__(self):
        return self.aboutProject


class Skill(models.Model):
    skillField = models.CharField(max_length=40)
    skilledIn = models.CharField(max_length=100)

    def __str__(self):
        return self.skillField

    def __str__(self):
        return self.skilledIn


class Interest(models.Model):
    interests = models.CharField(max_length=1000)

    def __str__(self):
        return self.interests


