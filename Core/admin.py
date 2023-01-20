from django.contrib import admin
from .models import FAQ, ContactUs, Subscriber, BlockedIP

admin.site.register(FAQ)
admin.site.register(ContactUs)
admin.site.register(Subscriber)
admin.site.register(BlockedIP)
