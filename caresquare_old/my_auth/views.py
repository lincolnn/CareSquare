# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpReponseRedirect("/")
    else:
        form = UserCreationForm()

    return render_to_response("register.html", {'form': form, })
