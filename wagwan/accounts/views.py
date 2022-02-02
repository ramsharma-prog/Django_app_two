from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.shortcuts import render, redirect
from django.contrib import messages
from . import models

from . import forms


# ACCOUNTS VIEW


class LoginPage(generic.CreateView):
    pass


class SignUp(generic.CreateView):

    form_class = forms.UserSignupForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class Profile(generic.TemplateView):
    model = models.Profile
    template_name = 'accounts/profile.html'


class UserUpdateView(generic.UpdateView):

    fields = ('username', 'email')
    model = User
    template_name = 'accounts/profile_form.html'

    def get_success_url(self):
        return reverse('profile')


def ImageUpdate(request):
    profile = request.user.profile
    image_form = forms.ImageUpdateForum(instance=profile)
    if request.method == "POST":

        image_form = forms.ImageUpdateForum(
            request.POST, request.FILES, instance=profile)

        if image_form.is_valid():
            image_form.save()

    context = {'image_form': image_form}
    return render(request, 'accounts/profile.html', context)


# def profile(request):
#     u_form = forms.UserUpdateForm(instance=request.user)
#     p_form = forms.ImageUpdateForum(instance=request.user.profile)
#     if request.method == "POST":
#
#         u_form = forms.UserUpdateForm(request.POST, instance=request.user)
#
#         p_form = forms.ImageUpdateForum(
#             request.POST, request.FILES, instance=profile)
#
#         if p_form.is_valid() and u_form.is_valid():
#             p_form.save()
#             u_form.save()
#             messages.success(request, 'Your profile has been updated')
#             return redirect('profile')
#
#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render(request, 'profile.html', context)
