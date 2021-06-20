from django.db import models
from django.db.models.deletion import CASCADE

class Users(models.Model):
    userId = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    #plate = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'users'

    def __str__(self):
        return self.userId, self.first_name, self.last_name

class Taxes(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users, on_delete=CASCADE)
    typeVeh = models.CharField(max_length=100)
    amount = models.FloatField()
    #next_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "taxes"

    def __str__(self):
        return self.id, self.typeVeh, self.amount, self.userId