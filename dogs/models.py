from django.db import models

class Dog(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    ]
    
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, blank=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='dog_photos/')
    needs_foster = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
