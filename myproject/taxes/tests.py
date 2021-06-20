from django.test import TestCase
from django.contrib.auth.models import User
from .models import Taxes

class PostModelTests(TestCase):
 

    def setUp(self):
        User.objects.create(
           first_name='MyName',
           last_name="MNySurname",
           email="testuser@test.com"
       )

    def test_taxes_add(self):
        user = User.objects.get(pk=1)
        taxes = Taxes(id=2, typeVeh= 'car', amount = 200)
        taxes.save()
        self.assertEquals(Taxes.objects.get(pk=1).amount, 200)