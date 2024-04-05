from email import message
from django.db import models

# Create your models here.

class regsave(models.Model):
    name = models.CharField(max_length=15,null=True,blank=False)
    mail = models.CharField(max_length=15,null=True,blank=False)
    mark = models.TextField(max_length=15,null=True,blank=False)
    number = models.TextField(max_length=15,null=True,blank=False)
    password = models.CharField(max_length=8,null=True,blank=False)
    re_pass = models.CharField(max_length=8,null=True,blank=False)

class logsave(models.Model):
    name = models.CharField(max_length=15,null=True,blank=False)
    password = models.CharField(max_length=8,null=True,blank=False)

class RegsaveG(models.Model):
    name = models.CharField(max_length=15,null=True,blank=False)
    mail = models.CharField(max_length=15,null=True,blank=False)
    course = models.TextField(max_length=15,null=True,blank=False)
    year = models.IntegerField(null=True,blank=False)
    number = models.TextField(max_length=15,null=True,blank=False)
    password = models.CharField(max_length=8,null=True,blank=False)
    re_pass = models.CharField(max_length=8,null=True,blank=False)

class RegsaveC(models.Model):
    name = models.CharField(max_length=15,null=True,blank=False)
    mail = models.CharField(max_length=15,null=True,blank=False)
    jobcate = models.TextField(max_length=15,null=True,blank=False)
    year = models.IntegerField(null=True,blank=False)
    number = models.TextField(max_length=15,null=True,blank=False)
    password = models.CharField(max_length=8,null=True,blank=False)
    re_pass = models.CharField(max_length=8,null=True,blank=False)    


class C_ADD_job1(models.Model):
    pname = models.TextField(max_length=200,null=True,blank=False)
    cname = models.TextField(max_length=500,null=True,blank=False)
    vaccancy = models.TextField(max_length=500,null=True,blank=False)
    place=models.TextField(max_length=500,null=True,blank=False)
    amount = models.IntegerField(null=True,blank=False)
    ex = models.TextField(max_length=500,null=True,blank=False) 
    qua = models.TextField(max_length=500,null=True,blank=False)  
    quan = models.TextField(max_length=500,null=True,blank=False)   
    des = models.TextField(max_length=500,null=True,blank=False)     
    img=models.ImageField(upload_to='image',null=True,blank=False)  
    # FF=models.FileField(upload_to='FileF/',null=True,blank=False)  

class G_ADD_guidance1(models.Model):
    gname = models.TextField(max_length=200,null=True,blank=False)
    number = models.IntegerField(null=True,blank=False)
    ctime = models.TextField(max_length=100,null=True,blank=False)
    place=models.TextField(max_length=500,null=True,blank=False)
    rfee = models.IntegerField(null=True,blank=False) 
    qua = models.TextField(max_length=500,null=True,blank=False)  
    quan = models.TextField(max_length=500,null=True,blank=False)   
    des = models.TextField(max_length=500,null=True,blank=False)     
    img=models.ImageField(upload_to='image',null=True,blank=False)        


class C_ADDed_detail(models.Model):
    pname = models.TextField(max_length=200,null=True,blank=False)
    cname = models.TextField(max_length=500,null=True,blank=False)
    vaccancy = models.TextField(max_length=500,null=True,blank=False)
    place=models.TextField(max_length=500,null=True,blank=False)
    amount = models.IntegerField(null=True,blank=False)
    ex = models.TextField(max_length=500,null=True,blank=False) 
    qua = models.TextField(max_length=500,null=True,blank=False)  
    quan = models.TextField(max_length=500,null=True,blank=False)   
    des = models.TextField(max_length=500,null=True,blank=False)     
    img=models.ImageField(upload_to='image',null=True,blank=False)    

class DETAIL_APPLY(models.Model):
    pname = models.TextField(max_length=200,null=True,blank=False)
    cname = models.TextField(max_length=500,null=True,blank=False)
    place=models.TextField(max_length=500,null=True,blank=False)
    amount = models.IntegerField(null=True,blank=False)
    qua = models.TextField(max_length=500,null=True,blank=False)  
    quan = models.TextField(max_length=500,null=True,blank=False)  
    sname = models.TextField(max_length=500,null=True,blank=False)
    ex = models.TextField(max_length=500,null=True,blank=False)
    gender = models.CharField(max_length=200,null=True,blank=False)
    cv = models.FileField(upload_to= 'file/',null=True,blank=False)           

class S_Details1(models.Model):
    sname = models.CharField(max_length=15,null=True,blank=False)
    email = models.CharField(max_length=15,null=True,blank=False)
    location = models.TextField(max_length=15,null=True,blank=False)
    year = models.IntegerField(null=True,blank=False)
    number = models.TextField(max_length=15,null=True,blank=False)
    cname = models.CharField(max_length=8,null=True,blank=False)
    img=models.ImageField(upload_to='image',null=True,blank=False)    

class C_USER1(models.Model):
    name = models.TextField(max_length=200,null=True,blank=False)
    pname = models.TextField(max_length=500,null=True,blank=False)
    email = models.TextField(max_length=500,null=True,blank=False)  
    number = models.TextField(max_length=500,null=True,blank=False)  
    message = models.TextField(max_length=500,null=True,blank=False)
    ex = models.TextField(max_length=500,null=True,blank=False)
    file = models.FileField(upload_to= 'file/',null=True,blank=False)  

class G_USER1(models.Model):
    name = models.TextField(max_length=200,null=True,blank=False)
    cname = models.TextField(max_length=500,null=True,blank=False)
    email = models.TextField(max_length=500,null=True,blank=False)  
    number = models.TextField(max_length=500,null=True,blank=False)  
    message = models.TextField(max_length=500,null=True,blank=False)
    qua = models.TextField(max_length=500,null=True,blank=False)
    file = models.FileField(upload_to= 'file/',null=True,blank=False)     

class C_Details(models.Model):
    pname = models.CharField(max_length=15,null=True,blank=False)
    month = models.CharField(max_length=15,null=True,blank=False)
    location = models.TextField(max_length=15,null=True,blank=False)
    cs = models.TextField(null=True,blank=False)
    number = models.TextField(max_length=15,null=True,blank=False)
    ctime = models.CharField(max_length=8,null=True,blank=False)
    img=models.ImageField(upload_to='image',null=True,blank=False)     