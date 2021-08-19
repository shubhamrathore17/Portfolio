from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, UpdateView, RedirectView, TemplateView, CreateView
from django.http import JsonResponse
from myportfolio import utils
from .models import Profile
from .forms import ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required



class TestTemplateView(TemplateView):

    template_name = 'index.html'
    queryset = Profile.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_profiles'] = self.queryset.all()
        context['last_profile'] = self.queryset.last()
        return context


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile_update_new.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context['last_profile'] = Profile.objects.last()
        pk = self.kwargs.get('pk', 0)
        profile = self.model.objects.get(id=pk)
        context['profile'] = profile
        if 'profile_form' not in context:
            context['profile_form'] = ProfileUpdateForm(instance=profile)
        return context

    def form_valid(self, form,*args, **kwargs):
        profile = form.save()
        messages.success(self.request,"Profile update successfully")
        return redirect('bearhug_folio')


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            authenticated = authenticate(username=username, password=password)
            if authenticated:
                auth_login(request, authenticated)
                # return redirect('profile_update')  
                return redirect('/profile/update/1/')
            else:
                messages.error(self.request, "Wrong username and password")
        return render(self.request, self.template_name)


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    pattern_name = 'login'
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class SendMessageView(View):

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # For Send mail on user email
        context = {'name': name,'email': email,'subject': subject,'message': message}
        utils.send_email(email, "Temporary Password {title}".format(title="Mr_bearhug.com"), context, 'email/connect_you.html', 'email/connect_you.txt')
        return JsonResponse({'status': 'success','name': name, 'email' : email, 'subject' : subject, 'message' :message })


