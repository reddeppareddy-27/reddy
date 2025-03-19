from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user_email = request.POST.get('email')  # User-provided email
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Email body to include form details
        email_body = f"""
        You have received a new message from the Contact Us form:
        Name: {name}
        Email: {user_email}
        Subject: {subject}
        Message: {message}
        """

        try:
            # Send the email
            send_mail(
                subject="New Contact Us Form Submission",  # Email subject
                message=email_body,
                from_email=user_email,  # User-provided email as sender
                recipient_list=['recipient_email@gmail.com'],  # Replace with recipient email
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")  # Success alert
        except Exception as e:
            messages.error(request, f"An error occurred while sending the email: {str(e)}")  # Error alert
        return redirect('contact_form')  # Redirect back to the form page

    return render(request, 'base/base.html')
