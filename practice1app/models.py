from django.db import models

# Create your models here.
class Member(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField("User Name",max_length=100)
    phone=models.CharField("Phone Number",max_length=20)
    email=models.EmailField("Email Address",max_length=100)
    passwd=models.CharField("password",max_length=20)

    def __str__(self):
        return self.username

    class Meta:
        db_table= "members"
