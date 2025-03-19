from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .models import Profile
import uuid
from base.emails import send_account_activation_email
from accounts.tokens import generate_reset_token  # Custom function for generating tokens
from base.emails import send_password_reset_email 


def profile_view(request):
    """Renders the profile page for authenticated users."""
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect unauthenticated users to login

    return render(request, 'accounts/profile.html', {'user': request.user})


def login_page(request):
    """Handles user login functionality."""
    if request.user.is_authenticated:
        return redirect('profile')  # Redirect if already logged in

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if user exists
        user_obj = User.objects.filter(username=email).first()
        if not user_obj:
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)

        # Ensure profile exists and check email verification
        profile, created = Profile.objects.get_or_create(user=user_obj)
        if not profile.is_email_verified:
            messages.warning(request, 'Your account is not verified. Please check your email.')
            return HttpResponseRedirect(request.path_info)

        # Authenticate the user
        user_obj = authenticate(username=email, password=password)
        if user_obj:
            login(request, user_obj)
            return redirect('/')  # Redirect to profile after login

        messages.warning(request, 'Invalid credentials.')
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/login.html')


def register_page(request):
    """Handles user registration functionality."""
    if request.user.is_authenticated:
        return redirect('/')  # Redirect if already logged in

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the email is already taken
        if User.objects.filter(username=email).exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        # Create the user
        user_obj = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=email
        )
        user_obj.set_password(password)
        user_obj.save()

        # Create or fetch the Profile
        profile, created = Profile.objects.get_or_create(user=user_obj)
        if created:
            profile.email_token = str(uuid.uuid4())  # Add the email token only if it's a new profile
            profile.save()

        # Send verification email
        send_account_activation_email(user_obj.email, profile.email_token)

        messages.success(request, 'An email has been sent for account verification.')
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/register.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def activate_email(request, email_token):
    """Handles email verification using the provided token."""
    try:
        # Get the profile by email token
        profile = get_object_or_404(Profile, email_token=email_token)

        # Check if the email is already verified
        if profile.is_email_verified:
            messages.info(request, 'Your email is already verified.')
            return redirect('login')

        # Verify the email
        profile.is_email_verified = True
        profile.email_token = None  # Clear the token after verification
        profile.save()

        messages.success(request, 'Your account has been successfully activated. You can now log in.')
        return redirect('login')
    except Exception as e:
        messages.error(request, f'Activation failed: {e}')
        return redirect('register')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Check if user exists with this email
        from django.contrib.auth.models import User
        user = User.objects.filter(email=email).first()
        if not user:
            messages.error(request, 'No account found with this email.')
            return render(request, 'accounts/forgot_password.html')

        # Generate token and send email
        from accounts.tokens import generate_reset_token  # Custom token generator
        token = generate_reset_token(user)
        from base.emails import send_password_reset_email
        send_password_reset_email(email, token)

        messages.success(request, 'Password reset email has been sent. Please check your inbox.')
        return render(request, 'accounts/forgot_password.html')

    return render(request, 'accounts/forgot_password.html')

def send_reset_email(request):
    """Handles sending the password reset email."""
    if request.method == 'POST':
        email = request.POST.get('email')

        # Check if the user exists with the given email
        user = User.objects.filter(email=email).first()
        if not user:
            messages.error(request, 'No account found with this email address.')
            return render(request, 'accounts/forgot_password.html')

        # Generate the reset token
        token = generate_reset_token(user)

        # Send the reset email
        send_password_reset_email(email, token)

        messages.success(request, 'Password reset email has been sent. Please check your inbox.')
        return render(request, 'accounts/forgot_password.html')

    return render(request, 'accounts/forgot_password.html')

def reset_password(request, token):
    from accounts.tokens import validate_reset_token  # Custom token validation logic
    user = validate_reset_token(token)
    if not user:
        messages.error(request, 'Invalid or expired token.')
        return redirect('forgot_password')

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect(request.path)

        user.set_password(new_password)
        user.save()
        messages.success(request, 'Password has been successfully reset.')
        return redirect('login')

    return render(request, 'accounts/reset_password.html', {'token': token})


