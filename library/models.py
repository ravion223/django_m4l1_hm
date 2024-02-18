from django.db import models

# Create your models here.

class LibraryBook(models.Model):
    title = models.CharField(max_length = 63)
    author = models.CharField(max_length = 63)
    isbn = models.CharField(max_length = 63, unique = True)
    available = models.BooleanField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["author"]