from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Transfer(models.Model):
    description = models.CharField(blank=True, max_length=100)
    amount = models.FloatField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)    
    incoming = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-date_added']

    def __unicode__(self):
        if self.incoming is True:
            return u"%s: %s %s" % (self.date_added, self.amount)
        else:
            return u"%s: %s %s" % (self.date_added, 0 - self.amount)
    
    def get_absolute_amount(self):
        if self.incoming is True:
            return self.amount
        else:
            return 0 - self.amount
                
