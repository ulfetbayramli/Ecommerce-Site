from django.urls import path
from .views import (AddressBook,
                    CustomLoginView,
                    CustomPasswordChangeView,
                    RegisterView,
                    CustomPasswordResetView,
                    CustomPasswordResetConfirmView,
                    CustomPasswordResetCompleteView,
                    CustomResetEmailConfirmView,
                    account_information,
                    activate,
                    )
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('change_info/<str:username>', account_information, name = "change_info"),
    path('change_password/', CustomPasswordChangeView.as_view(), name = "change_password"),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirmation/<str:uidb64>/<str:token>/', activate, name='confirmation'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<str:uidb64>/<str:token>',
        CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset/password_reset_email_confirm/',
        CustomResetEmailConfirmView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/password_reset_complete/',
        CustomPasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('address_book/', AddressBook.as_view(), name = "address_book"),
]