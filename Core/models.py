from django.db import models
from django.urls import reverse


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f'FAQ {self.id}'

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

class Subscriber(models.Model):
    email = models.EmailField()
    
    def __str__(self):
            return self.email

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"

class ContactUs(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.first_name}'s comment"
    
    def get_absolute_url(self):
        return reverse('contact_us')

    class Meta:
        verbose_name = "Contact Us Comment"
        verbose_name_plural = "Contact Us Comments"

class BlockedIP(models.Model):
    ip_addr = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.ip_addr

    class Meta:
        verbose_name = "BlockedIP"
        verbose_name_plural = "BlockedIPs"