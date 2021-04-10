from django.db import models

# Create your models here.
#class switch_panel(models.Model):
#    date=models.DateTimeField("date published")
#    def __str__(self):
#        return self.date

class switch(models.Model):
#    panel=models.ForeignKey(switch_panel,on_delete=models.CASCADE)
    switch_state=models.CharField(max_length=100, default="Some string")
    #switch_state2=models.BooleanField()
    #switch_state3=models.BooleanField()
    #switch_state4=models.BooleanField()
    def __str__(self):
        return self.switch_state