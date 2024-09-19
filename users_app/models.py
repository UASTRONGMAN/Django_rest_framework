from django.db import models

class UserModel(models.Model):
    class Meta:
        db_table = 'users'
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)