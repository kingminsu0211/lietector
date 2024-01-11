from django.db import models


class User(models.Model):
    id = models.CharField(max_length=30, primary_key=True, null=False)  # 30자 이하의 문자열
    password = models.CharField(max_length=30)  # 30자 이하의 문자열
    nickname = models.CharField(max_length=30)
    phonenumber = models.IntegerField()
    reports = models.TextField()
    blokings = models.TextField()


class Report(models.Model):
    reportnumber = models.IntegerField()
    reporttype = models.CharField(max_length=30)  # 30자 이하의 문자열
    reportdetails = models.TextField()
    blockingdetails = models.TextField()

class Diagnosis(models.Model):
    diagnosistype = models.TextField()
    phonedetails = models.TextField()
    diagnosisresults= models.IntegerField()
