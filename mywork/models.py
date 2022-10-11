from distutils.command.upload import upload
from time import timezone
from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model
from datetime import date,datetime
import uuid


# Create your models here

class testimonial(models.Model):
    details =models.CharField(max_length=10000)
    name =models.CharField(max_length=500)
    country =models.CharField(max_length=200, default=None)
    img =models.ImageField(upload_to='img%y')
    def __str__(self):
        return self.name

class investors_depo(models.Model):
    name =models.CharField(max_length=500)
    amt = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    coin = models.CharField(max_length=100, blank=True)
      
    def __str__(self):
        return self.name

    
class investors_payed(models.Model):
    name =models.CharField(max_length=500)
    amt = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    coin = models.CharField(max_length=100, blank=True)
     
    def __str__(self):
        return self.name




User = get_user_model()


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_user= models.IntegerField()
    code= models.CharField(max_length=12, blank=True)
    location = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    job = models.CharField(max_length=100, blank=True)
    mobile = models.IntegerField( blank=True, null=True)    
    profileimg = models.ImageField(upload_to='profile_images', default='t.png')
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True,related_name='ref_by')
    


    def __str__(self):
        return self.user.username
                     


class payment1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    amt1 = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    coin1 =models.CharField(max_length=50,blank=True)
    trans_date1 = models.DateTimeField(default=datetime.now, blank=True)
    bol = models.BooleanField('successful',null=True)

 
    
    def __str__(self):
        return f'{self.user.username}-{self.coin1}'

class investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    amt1 = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    plans = models.CharField(max_length=100, blank=True)
    trans_date1 = models.DateTimeField(default=datetime.now, blank=True)
    bol = models.BooleanField('completed',default=False)

    def __str__(self):
        return f'{self.user.username}-{self.plans}'

   


class wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    wallet_ad = models.CharField(max_length=100)
    coin = models.CharField(max_length=100, blank=True)
    

    def __str__(self):
        return f'{self.user.username}-{self.coin}'


class withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    amt = models.DecimalField(max_digits=9, decimal_places=2, blank=True,null=True)
    wallet_ad = models.CharField(max_length=100)
    trans_date1 = models.DateTimeField(default=datetime.now, blank=True)
    withdrw = models.BooleanField('successful',null=True)


    def __str__(self):
        return f'{self.user.username}-{self.amt}'


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message= models.TextField()
    subject=models.CharField(max_length=200)    

    def __str__(self):
        return self.name

class percentage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    amt = models.DecimalField(max_digits=9, decimal_places=2, blank=True,null=True)

    def __str__(self):
        return f'{self.user.username}-{self.amt}'





    
    


    
   
            
