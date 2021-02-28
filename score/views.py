from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, FormView
from . import forms
from django.urls import reverse_lazy
from .sample import RhymeSearch

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "login.html"

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "logout.html"

class MyCreateView(CreateView):
    form_class = forms.CreateUser
    template_name = "create.html"
    success_url = reverse_lazy("login")

class IndexView(FormView):
    form_class = forms.RhymeText
    template_name = "index.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.user =  self.request.user
        RS = RhymeSearch()
        ori, ans = RS.main(form.instance.text)
        print(ans)
        form.save()  # 保存処理など
        return super().form_valid(form)