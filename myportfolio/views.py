from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, UpdateView, DeleteView, TemplateView, CreateView
from django.http import JsonResponse
from myportfolio import utils


class TestTemplateView(TemplateView):

    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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
