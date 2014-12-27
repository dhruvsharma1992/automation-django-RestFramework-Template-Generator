from django.db import models

class sampleModel(models.Model):
    
    textField = models.CharField()
    intField = models.IntegerField()
    def create(self,text,integer):
        self.textField=text
        self.integerField=integer
