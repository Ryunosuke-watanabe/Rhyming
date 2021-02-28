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

# ans = None

class IndexView(FormView):
    form_class = forms.RhymeText
    template_name = "index.html"
    # success_url = reverse_lazy("index")
    def form_valid(self, form):
        form.instance.user =  self.request.user
        form.save()  # 保存処理など
        # return super().form_valid(form)
        return render(self.request, 'index.html', form)

class ResultView(FormView):
    form_class = forms.RhymeText

    def form_valid(self, form):
        RS = RhymeSearch()
        ans = form.instance.text
        context = RS.main(ans)
        # print(context)
        return render(self.request, 'result.html',  {'form': context, 'text': form})

    def form_invalid(self, form):
        return render(self.request, 'index.html', {'form': form})