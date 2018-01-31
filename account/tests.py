from django.test import TestCase
from django.test import TestCase
from account import models as amod

class UserModelTest(TestCase):
    def setUp(self):
        self.u1 = amod.User()
        self.u1.first_name = "Marge"
        self.u1.last_name = "Simpson"
        self.u1.email = "marge@simpsons.com"
        self.u1.set_password('password')
        #... More fields
        self.u1.save()


    def test_user_create_save_load(self):
        '''Tests round trip of user model to from database'''
        u2 = amod.User.objects.get(email=u1.email)
        self.assertEquals(u1.first_name, u2.first_name)
        self.assertEquals(u1.last_name, u2.last_name)
        self.assertEquals(u1.email, u2.email)
        self.assertEquals(u1.password, u2.password)

    def test_passwords(self):
        '''Test to make sure that passwords function correctly'''
        u2 = amod.User.objects.get(email=u1.email)
        self.assertTrue(u2.check_password("password"))
