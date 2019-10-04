from django.db import models


class Customers(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.EmailField(default='abc@abc.com')
    rating = models.IntegerField(default=-1)
    time_taken = models.CharField(max_length=50)
    suggestion = models.CharField(max_length=300)

    def __str__(self):
        return self.name
