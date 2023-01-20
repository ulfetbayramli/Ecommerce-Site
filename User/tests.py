from django.test import TestCase
from .models import User

class TestModels(TestCase):

    @classmethod
    def setUpClass(cls):

        cls.data1 = {
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "email": "johndoe@gmail.com"
        }
        cls.user = User.objects.create(**cls.data1)

    def test_user(self):
        with self.subTest():
            self.assertEqual(self.data1['first_name'], self.user.first_name)
        with self.subTest():
            self.assertEqual(self.data1['last_name'], self.user.last_name)
        with self.subTest():
            self.assertEqual(self.data1['username'], self.user.username)
        with self.subTest():
            self.assertEqual(self.data1['email'], self.user.email)
    
    @classmethod
    def tearDownClass(cls):
        del cls.user
