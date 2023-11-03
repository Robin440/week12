from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    def __str__(self):
        return "%s %s %s %s %s" % (self.username,self.fname, self.lname,self.mobile, self.email)