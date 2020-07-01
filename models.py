from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=150)
    mail = models.CharField(max_length=200)
    phone = models.CharField(max_length=20) 
    psw = models.CharField(max_length=15)
    pswr = models.CharField(max_length=15)

# my django admin username for this project is = Ejike_Sylva
# my email address is ajike263@gmail.com
# my password is 8622929815141451

    def __str__(self):
        return self.name
