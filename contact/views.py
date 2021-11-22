from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from profiles.models import UserProfile
from .forms import OrderInquiryForm

# Create your views here.


def order_inquiry(request):
    """ Allow users to send order enquiries """
    user_email = request.POST.get('contact_email')
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        inquiry_form = {
            'name': request.POST.get('name'),
            'contact_email': request.POST.get('contact_email'),
            'order_number': request.POST.get('order_number'),
            'message': request.POST.get('message'),
        }
        # send email
        subject = render_to_string(
            'order_inquiry/order_inquiry_emails/inquiry_subject.txt',
            {'inquiry': inquiry_form}
        )
        body = render_to_string(
            'order_inquiry/order_inquiry_emails/inquiry_body.txt',
            {'inquiry': inquiry_form}
        )
        send_mail(
            subject, body, user_email, [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False
        )
        messages.success(request, 'Inquiry Successfully Sent!')

    form = OrderInquiryForm
    orders = profile.orders.all()

    context = {
        'form': form,
        'on_profile_page': True,
        'orders': orders,
        }
    return render(request, 'order_inquiry/order_inquiry.html', context)
