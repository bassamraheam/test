from django.db import models

# Create your models here.
class Product(models.Model):
    PRDName = models.CharField(max_length=100)
    #category
    PRDDesc = models.TextField()
    PRDPrice = models.DecimalField(max_digits=5,decimal_places=2)
    PRDCost = models.DecimalField(max_digits=5,decimal_places=2)
    PRDCreated = models.DateTimeField()

    def __str__(self):
        return self.PRDName