from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, UpdateView

from accounts.forms import SignUpForm, UserUpdateForm, PasswordChangeForm


def register_view(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            # User.objects.create(user=user)
            login(request, user)
            return redirect('webapp:index')
        else:
            return render(request, 'register.html', {'form': form})


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'


class UserChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_update.html'
    context_object_name = 'user_obj'
    form_class = UserUpdateForm

    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})


class UserChangePasswordView(UserChangeView):
    template_name = 'user_change_pass.html'
    form_class = PasswordChangeForm

    def get_success_url(self):
        return reverse('accounts:login')
