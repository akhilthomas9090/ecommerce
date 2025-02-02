from django.db import models

# Create your models here.

class Contact(models.Model):
    # contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    description=models.TextField(max_length=500)
    phone_number=models.IntegerField()


    def __str__(self):
        return self.name
    


class Product(models.Model):
    product_id= models.AutoField
    product_name = models.CharField(max_length=100)
    category= models.CharField(max_length=100,default="")
    subcatergory= models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)


    image=models.ImageField(upload_to='images/images')

    def __str__(self):
        return self.product_name    
    

    # def __int__(self):
    #     return self.product_id   check it later 