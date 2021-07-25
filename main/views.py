from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    if request.method == "POST":
        contact_name = request.POST['contact_name']
        contact_phone = request.POST['contact_phone']
        contact_email = request.POST['contact_email']
        contact_message = request.POST['contact_message']

        #send an email
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

        return render(request, "home.html", {'contact_name':contact_name})
    else:
        return render(request, "home.html", {})

def kursy(request):
    return render(request, "kursy.html", {})


# Create your views here.
