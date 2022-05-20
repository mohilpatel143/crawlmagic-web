from django.shortcuts import render
from .models import Subscrib, Contact
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method=="POST":
        email = request.POST.get('email', '')
        subscrib = Subscrib(email=email)
        subscrib.save()

        send_mail('Welcome user',                      # subject
        f"{email} Came in Contact With Our Site.",     # message
        'mohil.crawlmagic@gmail.com',                  # from
        ['patelmohil143@gmail.com'],                   # to
        fail_silently=False)
    return render(request, 'webapp/index.html')


def services(request):
    return render(request, 'webapp/services.html')

def pricing(request):
    return render(request, "webapp/services.html")

def itsolution(request):
    return render(request, 'webapp/index-9.html')

def aboutus(request):
    return render(request, 'webapp/about-us.html')

def contactus(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        contact = Contact(first_name=first_name, last_name=last_name, phone=phone, email=email, message=message)
        contact.save()

        send_mail('Contact Details',
                  f"{first_name} {last_name}'s Data Received",
                  'mohil.crawlmagic@gmail.com',               
                  ['patelmohil143@gmail.com'], 
                  fail_silently=False)
    return render(request, 'webapp/contact-us.html')

def career(request):
    return render(request, 'webapp/career.html')

def support(request):
    return render(request, 'webapp/support.html')

def notfound(request):
    return render(request, 'webapp/404.html')
