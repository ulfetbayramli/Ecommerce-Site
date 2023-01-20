from django.test import TestCase
from .models import FAQ, Subscriber, ContactUs, BlockedIP

class TestModels(TestCase):

    @classmethod
    def setUpClass(cls):

        cls.data1 = {
            "question": "How are you?",
            "answer": "I'm fine!"
        }
        cls.faq = FAQ.objects.create(**cls.data1)

        cls.data2 = {
            "email": "emilywatson@gmail.com"
        }
        cls.subscriber = Subscriber.objects.create(**cls.data2)

        cls.data3 = {
            "first_name": "Emily",
            "last_name": "Watson",
            "telephone": "+994778889911",
            "email": "emilywatson@gmail.com",
            "comment": "Test is working!"
        }
        cls.contact = ContactUs.objects.create(**cls.data3)

        cls.data4 = {
            "ip_addr": "10.0.0.20"
        }
        cls.blockedIP = BlockedIP.objects.create(**cls.data4)

    def test_faq(self):
        with self.subTest():
            self.assertEqual(self.data1['question'], self.faq.question)
        with self.subTest():
            self.assertEqual(self.data1['answer'], self.faq.answer)

    def test_subscriber(self):
        self.assertEqual(self.data2['email'], self.subscriber.email)
    
    def test_contact(self):
        with self.subTest():
            self.assertEqual(self.data3['first_name'], self.contact.first_name)
        with self.subTest():
            self.assertEqual(self.data3['last_name'], self.contact.last_name)
        with self.subTest():
            self.assertEqual(self.data3['telephone'], self.contact.telephone)
        with self.subTest():
            self.assertEqual(self.data3['email'], self.contact.email)
        with self.subTest():
            self.assertEqual(self.data3['comment'], self.contact.comment)

    def test_blockedIP(self):
        self.assertEqual(self.data4['ip_addr'], self.blockedIP.ip_addr)

    @classmethod
    def tearDownClass(cls):
        del cls.faq
        del cls.subscriber
        del cls.contact
        del cls.blockedIP
