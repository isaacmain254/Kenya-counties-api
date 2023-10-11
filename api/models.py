from django.db import models

class County(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code =  models.PositiveIntegerField(unique=True, blank=True, null=True)
    logo = models.ImageField(upload_to='images/', blank=True)
    capital = models.CharField(max_length=200, blank=True)
    population= models.PositiveIntegerField()
    
    
    class Meta:
        verbose_name_plural = 'counties'

    def __str__(self):
        return self.name
    
    
class Subcounty(models.Model):
    county = models.ForeignKey(County, related_name='sub_counties', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    population = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'subcounties'

    def __str__(self):
        return self.name