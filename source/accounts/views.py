from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm


def register_view(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            User.objects.create(user=user)
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'register.html', {'form': form})