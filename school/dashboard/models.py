from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.TextField(db_column='name',null=True)
    mob=models.BigIntegerField(db_column='mob',null=True)
    email=models.TextField(db_column='email',null=True)
    repass=models.TextField(db_column='password',null=True)


class Course(models.Model):       
        title=models.TextField(db_column='title',null=True)
        description=models.TextField(db_column='email',null=True)
        price=models.PositiveIntegerField(db_column='message',null=True)
        image=models.ImageField(null=True)