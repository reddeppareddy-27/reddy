from django.urls import path
from accounts.views import login_page, register_page, profile_view, activate_email,logout_view,forgot_password, send_reset_email, reset_password

urlpatterns = [
    path('login/', login_page, name="login"),  # Handles user login
    path('logout/', logout_view, name='logout'),

    path('register/', register_page, name="register"),  # Handles user registration
    path('profile/', profile_view, name="profile"),  # Displays the profile page
    path('activate/<str:email_token>/', activate_email, name="activate_email"),  # Activates the account via email token
    path('forgot_password/', forgot_password, name='forgot_password'),  # Page to enter email
    path('send-reset-email/', send_reset_email, name='send_reset_email'),  # Sends the email
    path('reset-password/<str:token>/', reset_password, name='reset_password'),  # Resets the password
]
