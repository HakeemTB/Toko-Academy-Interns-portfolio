from django.shortcuts import render,  redirect
from django.contrib import messages
from .models import Interns,  ContactMessage
from .task import send_contact_email_notification
from .forms import ContactForm


@ratelimit(key='ip', rate='5/m', block=True)
# Create your views here.
def index_view(request):
    if request.method == 'POST':
        #Extract  field content from form
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')



        #Basic server-side validation check
        if full_name and email and message:
            ContactMessage.objects.create(
                full_name=full_name,
                email=email,
                message=message,
                subject=subject
            )

            messages.success(request, "Your  message has been securely submitted")
            return redirect('index')
        else:
            messages.error(request, "Please fill in all mandatory fields")

    #Context delivey for GET requests
    interns = Interns.objects.all().order_by('name')
    context = {
        'interns':interns
    }
    return render(request, 'index.html', context)