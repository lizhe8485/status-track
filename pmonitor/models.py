from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Status(models.Model):
#    comp_id    = models.AutoField(primary_key=True)
    SampleName  = models.CharField(max_length=200)
    MethodGeneration  = models.CharField(max_length=200)
    DAMethodGeneartion  = models.CharField(max_length=200)
    Acquisition  = models.CharField(max_length=200)
    FileMover  = models.CharField(max_length=200)
    Preprocess  = models.CharField(max_length=200)
    DataAnalysis  = models.CharField(max_length=200)
    ReportReader  = models.CharField(max_length=200)
    CSVGeneration  = models.CharField(max_length=200)
    postProcess  = models.CharField(max_length=200)
    #statusCode = models.IntegerField()
    #comment    = models.TextField()
    #created_on = models.DateTimeField(auto_now_add=True, null=False)
    #created_timezone = timezone.now()

#    def update(self):
#        self.update_time = timezone.now()
#        self.save()

    def __str__(self):
        return self.SampleName

    def _get_status(self):
     return [self.SampleName,self.MethodGeneration,self.DAMethodGeneartion,self.Acquisition,self.FileMover,self.Preprocess,self.DataAnalysis,self.ReportReader,self.CSVGeneration,self.postProcess]
    aStatusList = property(_get_status)
