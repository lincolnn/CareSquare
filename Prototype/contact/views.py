from django.shortcuts import redirect, render
from django.core.mail import mail_admins
from forms import ContactForm

def contact_form(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            message = "From: %s <%s>\r\nSubject:%s\r\nMessage:\r\n%s\r\n" % (
                form.cleaned_data['name'],
                form.cleaned_data['email'],
                form.cleaned_data['subject'],
                form.cleaned_data['message']
            )
            mail_admins('Contact form', message, fail_silently=False)
            if request.is_ajax():
                return render(request, 'contact/success.html')
            else:
                return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact/form.html', {'form':form})
