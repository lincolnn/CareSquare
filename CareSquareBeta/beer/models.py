from django.db import models

BEER_CHOICES = (
        ('D', 'Domestic'), #('G', 'Good')
        ('I', 'Import'), #('S', 'SoSo') + ('B', 'Bad')
)

class Beer(models.Model): # = Member
    name                = models.CharField(max_length=200)
    slug                = models.SlugField(unique=True)
    brewery             = models.ForeignKey('Brewery') # ForeignKey('CareCoordinator')
    locality            = models.CharField(max_length=1, choices=BEER_CHOICES) # swap with choices of mood
    description         = models.TextField(blank=True) # blank=True makes it optional

    def __unicode__(self):  # always define a unicode object for self
        return self.name # return name field as the definition of itself

class Brewery(models.Model): # replace with CareCoordinator
    name                =  models.CharField(max_length=200)
    slug                = models.SlugField(unique=True)
    description         = models.TextField(blank=True)
    
    def __unicode__(self):
            return self.name
