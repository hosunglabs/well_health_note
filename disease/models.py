from django.db import models
from django.utils import timezone

# Create your models here.
class Disease(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    definition = models.TextField(blank = True, null = True)
    definition_image = models.FileField(blank = True, null = True)
    symptom = models.TextField(blank = True, null = True)
    symptom_image = models.FileField(blank = True, null = True)
    diagnosis = models.TextField(blank = True, null = True)
    diagnosis_image = models.FileField(blank = True, null = True)
    treatment = models.TextField(blank = True, null = True)
    treatment_image = models.FileField(blank = True, null = True)
    prognosis = models.TextField(blank = True, null = True)
    prognosis_image = models.FileField(blank = True, null = True)
    common = models.TextField(blank = True, null = True)
    common_image = models.FileField(blank = True, null = True)
    drug = models.TextField(blank = True, null = True)
    drug_image = models.FileField(blank = True, null = True)
    article = models.TextField(blank = True, null = True)
    published_date = models.DateTimeField(default = timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Symptom(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    diagnosis = models.TextField(blank = True, null = True)
    diagnosis_image = models.FileField(blank = True, null = True)
    treatment = models.TextField(blank = True, null = True)
    treatment_image = models.FileField(blank = True, null = True)
    article = models.TextField(blank = True, null = True)
    published_date = models.DateTimeField(default = timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Treatment(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default = timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Drug(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    definition = models.TextField()
    effect = models.TextField(blank = True, null = True)
    method = models.TextField(blank = True, null = True)
    ban = models.TextField(blank = True, null = True)
    caution = models.TextField(blank = True, null = True)
    side_effect = models.TextField(blank = True, null = True)
    published_date = models.DateTimeField(default = timezone.now)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
