from django.db import models

class Gundam(models.Model):
    SIZE_CHOICES = [
        ('SD', 'Super Deformed'),
        ('HG', 'High Grade'),
        ('RG', 'Real Grade'),
        ('MG', 'Master Grade'),
        ('PG', 'Perfect Grade'),
        ('Mega', 'Mega Size'),
    ]

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gundam_images/')
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)

    def __str__(self):
        return self.name
