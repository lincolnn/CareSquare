from django.db import models

RATING_CHOICES = (
        ('G', 'Good'),
        ('S', 'SoSo'),
        ('B', 'Bad'),
)

### Checkin Models
class CareCoordinator(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.first_name

class Member(models.Model):
    carecordinator = models.ForeignKey(CareCoordinator) # link to CC
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    slug = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.last_name

class Checkin(models.Model):
    publication_date = models.DateField()
    member = models.ForeignKey(Member)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    description = models.TextField(blank=True)

    def __unicode__(self): # define unicode version for every class
            return self.member
